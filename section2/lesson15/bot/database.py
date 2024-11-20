import sqlite3

connection = sqlite3.connect('delivery.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER, name TEXT, number TEXT UNIQUE);')
sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, '
            'description TEXT, price REAL, quantity INTEGER, photo TEXT);')
sql.execute('CREATE TABLE IF NOT EXISTS cart '
            '(user_id INTEGER, user_product TEXT, quantity INTEGER);')


def register_user(tg_id, name, number):
    sql.execute('INSERT INTO users (id, name, number) VALUES (?, ?, ?);',
                (tg_id, name, number))
    connection.commit()


def is_user_registered(tg_id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (tg_id,)).fetchone():
        return True
    return False


def get_all_products():
    return sql.execute('SELECT * FROM products;').fetchall()


def get_available_products():
    products = sql.execute('SELECT id, name, quantity '
                           'FROM products;').fetchall()
    available_products = [product for product in products if product[2] > 0]

    return available_products


def get_product(product_id):
    return sql.execute('SELECT * FROM products WHERE id=?;',
                       (product_id,)).fetchone()


def get_price(product_name):
    return sql.execute('SELECT price FROM products WHERE name=?;',
                       (product_name,)).fetchone()


def add_to_cart(user_id, user_product, quantity):
    sql.execute('INSERT INTO cart VALUES (?, ?, ?);',
                (user_id, user_product, quantity))
    connection.commit()


def clear_cart(user_id):
    sql.execute('DELETE FROM cart WHERE user_id=?;', (user_id,))
    connection.commit()


def show_cart(user_id):
    return sql.execute('SELECT * FROM cart WHERE user_id=?;',
                       (user_id,)).fetchall()


def make_order(user_id):
    user_cart_products = sql.execute('SELECT user_product '
                                     'FROM cart WHERE user_id=?;',
                                     (user_id,)).fetchall()
    user_cart_quantities = sql.execute('SELECT quantity '
                                       'FROM cart WHERE user_id=?;',
                                       (user_id,)).fetchall()
    available_quantities = [
        sql.execute('SELECT quantity FROM products WHERE name=?;',
                    (i[0],)).fetchone()[0] for i in user_cart_products]
    totals = []
    # i - how many the user has taken
    for i in user_cart_quantities:
        # j - quantity from stock
        for j in available_quantities:
            totals.append(j - i[0])

    # t - changed product quantity
    for t in totals:
        # n - products name
        for n in user_cart_products:
            sql.execute('UPDATE products SET quantity=? WHERE name=?;',
                        (t, n[0]))
    connection.commit()
    return available_quantities, totals
