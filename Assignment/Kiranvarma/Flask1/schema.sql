DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

INSERT INTO users (username, password, email) VALUES (
    "user",
    "userpass",
    "user@gmail.com"
);