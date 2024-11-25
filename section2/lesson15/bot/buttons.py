from telebot import types


def send_number_button():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Send number📞', request_contact=True)
    keyboard.add(button)

    return keyboard


def show_main_menu(products):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    cart = types.InlineKeyboardButton('Cart🛒', callback_data='cart')
    all_products = [
        types.InlineKeyboardButton(f'{i[1]}', callback_data=i[0])
        for i in products]
    keyboard.add(*all_products)
    keyboard.row(cart)

    return keyboard


def select_quantity(product_quantity, operation='', quantity=1):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    minus = types.InlineKeyboardButton('-', callback_data='decrement')
    counter = types.InlineKeyboardButton(str(quantity),
                                         callback_data=str(quantity))
    plus = types.InlineKeyboardButton('+', callback_data='increment')
    add_to_cart = types.InlineKeyboardButton('Add To Cart🛒',
                                             callback_data='add_to_cart')
    back = types.InlineKeyboardButton('Back', callback_data='back')

    if operation == 'increment':
        if quantity <= product_quantity:
            counter = types.InlineKeyboardButton(str(quantity + 1),
                                                 callback_data=str(
                                                     quantity + 1))
    elif operation == 'decrement':
        if quantity > 1:
            counter = types.InlineKeyboardButton(str(quantity - 1),
                                                 callback_data=str(
                                                     quantity - 1))

    keyboard.add(minus, counter, plus)
    keyboard.row(back, add_to_cart)

    return keyboard


def cart_buttons():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    order = types.InlineKeyboardButton('Make an order', callback_data='order')
    clear = types.InlineKeyboardButton('Clear cart', callback_data='clear')
    back = types.InlineKeyboardButton('Back', callback_data='back')

    keyboard.add(order, clear)
    keyboard.row(back)

    return keyboard


def send_location_button():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Send location🗺️', request_location=True)
    keyboard.add(button1)

    return keyboard


def admin_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Add product')
    button2 = types.KeyboardButton('Delete product')
    button3 = types.KeyboardButton('Change product')
    button4 = types.KeyboardButton('Go to main menu')

    keyboard.add(button1, button2, button3)
    keyboard.row(button4)

    return keyboard
