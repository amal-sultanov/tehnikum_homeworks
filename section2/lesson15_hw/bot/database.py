import sqlite3

connection = sqlite3.connect('users.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER, name TEXT, number TEXT UNIQUE, '
            'latitude REAL, longitude REAL);')


def register_user(tg_id, name, number, latitude, longitude):
    sql.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?);',
                (tg_id, name, number, latitude, longitude))
    connection.commit()


def is_user_registered(tg_id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (tg_id,)).fetchone():
        return True
    return False
