from telebot import types


def menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Wikipedia')
    button2 = types.KeyboardButton('Translator')
    keyboard.add(button1, button2)

    return keyboard
