from telebot import types


def send_number_button():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Send number📞', request_contact=True)
    keyboard.add(button)

    return keyboard


def send_location_button():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Send location🗺️', request_location=True)
    keyboard.add(button)

    return keyboard
