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
    updated_quantities = []

    for cart_quantity in user_cart_quantities:
        for quantity in available_quantities:
            updated_quantities.append(quantity - cart_quantity[0])

    for quantity in updated_quantities:
        for product_name in user_cart_products:
            sql.execute('UPDATE products SET quantity=? WHERE name=?;',
                        (quantity, product_name[0]))
    connection.commit()

    return available_quantities, updated_quantities


def add_product(name, description, price, quantity, photo):
    if (name,) in sql.execute('SELECT name FROM products;').fetchall():
        return False
    sql.execute('INSERT INTO products '
                '(name, description, price, quantity, photo) '
                'VALUES (?, ?, ?, ?, ?);',
                (name, description, price, quantity, photo))
    connection.commit()


def delete_product(product_name):
    sql.execute('DELETE FROM products WHERE name=?;', (product_name,))
    connection.commit()


def change_attribute(current_value, new_value, attribute=''):
    if attribute == 'name':
        sql.execute('UPDATE products SET name=? WHERE name=?;',
                    (new_value, current_value))
    elif attribute == 'description':
        sql.execute('UPDATE products SET description=? WHERE name=?;',
                    (new_value, current_value))
    elif attribute == 'price':
        sql.execute('UPDATE products SET price=? WHERE name=?;',
                    (new_value, current_value))
    elif attribute == 'quantity':
        sql.execute('UPDATE products SET quantity=? WHERE name=?;',
                    (new_value, current_value))
    elif attribute == 'photo':
        sql.execute('UPDATE products SET photo=? WHERE name=?;',
                    (new_value, current_value))
    connection.commit()


def check_products():
    if sql.execute('SELECT * FROM products;').fetchall():
        return True
    return False
