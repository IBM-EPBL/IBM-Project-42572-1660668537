import sqlite3
conn=sqlite3.connect('user.db')

print("Opened Database")

conn.execute('CREATE TABLE user(name TEXT,email TEXT,password TEXT)')
print('Table created')

conn.close()