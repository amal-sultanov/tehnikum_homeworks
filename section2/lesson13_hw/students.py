import sqlite3

connection = sqlite3.connect('mydatabase.db')
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS students "
            "(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT);")
sql.execute("INSERT INTO students (name, age, grade) "
            "VALUES ('Alice', 25, 'A+');", )
sql.execute("INSERT INTO students (name, age, grade) "
            "VALUES ('Adam', 43, 'B');", )


def get_student_by_name(name):
    result = sql.execute("SELECT * FROM students WHERE name=?;", (name,))
    return result.fetchone()


def update_student_grade(name, grade):
    sql.execute("UPDATE students SET grade=? WHERE name =?;", (grade, name))


def delete_student(name):
    sql.execute("DELETE FROM students WHERE name=?;", (name,))


def close_connection():
    connection.close()


connection.commit()
