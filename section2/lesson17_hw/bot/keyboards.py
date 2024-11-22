from telebot import types


def send_language_buttons():
    keyboard = types.InlineKeyboardMarkup()
    ru_button = types.InlineKeyboardButton('🇷🇺Русский', callback_data='ru')
    uz_button = types.InlineKeyboardButton('🇺🇿O‘zbekcha', callback_data='uz')
    keyboard.add(ru_button, uz_button)

    return keyboard


def send_number_button(button_text):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(f'{button_text}📞', request_contact=True)
    keyboard.add(button)

    return keyboard


def send_location_button(button_text):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(f'{button_text}🗺️', request_location=True)
    keyboard.add(button)

    return keyboard
