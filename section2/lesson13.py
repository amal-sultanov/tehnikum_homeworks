import sqlite3

connection = sqlite3.connect('my_users.db')
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT);")
sql.execute("INSERT INTO users (id, name) VALUES (1, 'Bob');")
sql.execute("INSERT INTO users (id, name) VALUES (2, 'David');")
print(sql.execute("SELECT id FROM users;").fetchall())
print(sql.execute("SELECT id FROM users;").fetchone())
print(sql.execute("SELECT * FROM users WHERE id=2;").fetchone())
sql.execute("DELETE FROM users WHERE id=1;")
print(sql.execute("SELECT id FROM users;").fetchall())
sql.execute("UPDATE users SET name='Jack' WHERE id=2;")
print(sql.execute("SELECT * FROM users;").fetchall())

connection.commit()
connection.close()
