from flask import Flask,render_template,request,redirect,session

import sqlite3

app=Flask(__name__)

def init_db():
    db = sqlite3.connect('users.db')
    with open('schema.sql', 'r') as schema:
        db.executescript(schema.read())
    db.commit()

@app.cli.command('initdb')
def initdb_cmd():
    init_db()
    print("Initialised database.")

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    db = get_db()
    db.execute('CREATE TABLE users ( id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL)')
    db.commit()
    return render_template("index.html")

@app.route("/index")
def index():
    app.logger.info('hone')
    initdb_cmd()
    return render_template("index.html")


@app.route('/signin', methods=('GET', 'POST'))
def signin():
    error = None
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT password FROM users WHERE username = ?', (username, )
        ).fetchone()
        
        if user is None:
            error = 'Incorrect Username/Password.'
        elif password != user['password']:
            print(user)
            error = 'Incorrect Password.'

        if error is None:
            return redirect(url_for('index'))
        flash(error)
        db.close()
    return render_template('signin.html', title='Sign In', error=error)

@app.route('/signup', methods=('POST', 'GET'))
def signup():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        email = request.form['email']
        db = get_db()
        curr = db.cursor()
        
        curr.execute(
            'INSERT INTO users (username, password, email) VALUES (?, ?, ?);', (username, password, email)
        )
        db.commit()
        curr.close()
        db.close()
        return render_template('index.html', title="Home", succ="Registration Successfull!")
        

    return render_template('signup.html', title='Sign Up')
