import sqlite3

connection = sqlite3.connect('users.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER, name TEXT, number TEXT UNIQUE, '
            'latitude REAL, longitude REAL, language TEXT);')


def register_user(tg_id, name, number, latitude, longitude, language):
    sql.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?);',
                (tg_id, name, number, latitude, longitude, language))
    connection.commit()


def is_user_registered(tg_id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (tg_id,)).fetchone():
        return True
    return False


def get_language(tg_id):
    result = sql.execute('SELECT language FROM users WHERE id=?;',
                         (tg_id,)).fetchone()

    return result[0]


def change_language(tg_id, new_language):
    sql.execute('UPDATE users SET language=? WHERE id=?;',
                (new_language, tg_id))
    connection.commit()
