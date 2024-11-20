from telebot import types


def send_number_button():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Send number📞', request_contact=True)
    keyboard.add(button)

    return keyboard


def show_main_menu(products):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    cart = types.InlineKeyboardButton('Cart🛒', callback_data='cart')
    all_products = [types.InlineKeyboardButton(f'{i[1]}', callback_data=i[0])
                    for i in products]
    keyboard.add(*all_products)
    keyboard.row(cart)

    return keyboard
