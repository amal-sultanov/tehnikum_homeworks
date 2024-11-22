import requests
import telebot
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
                     f'Hi, @{message.from_user.username}!\n'
                     f'Enter the amount of UZS you want to convert:')


@bot.message_handler(content_types=['text'])
def check_amount(message):
    if message.text.isnumeric():
        amount = message.text
        bot.send_message(message.from_user.id,
                         'What is your desirable currency?',
                         reply_markup=show_menu())
        bot.register_next_step_handler(message, convert_currency, amount)
    else:
        bot.send_message(message.from_user.id, 'Enter a number:')
        bot.register_next_step_handler(message, check_amount)


def convert_currency(message, amount):
    symbol = message.text
    url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'
    response = requests.get(url).json()
    euro_rate = response[1]['Rate']
    dollar_rate = response[0]['Rate']
    rouble_rate = response[2]['Rate']
    conversions = {
        '€': int(amount) / float(euro_rate),
        '$': int(amount) / float(dollar_rate),
        '₽': int(amount) / float(rouble_rate)
    }

    if symbol in conversions:
        bot.send_message(message.from_user.id,
                         f'{amount} of UZS is equal to '
                         f'{symbol}{conversions[symbol]:.2f}',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.from_user.id,
                         'No such currency, select from available')
        bot.register_next_step_handler(message, convert_currency, amount)


def show_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('€')
    button2 = types.KeyboardButton('$')
    button3 = types.KeyboardButton('₽')
    keyboard.add(button1, button2, button3)

    return keyboard


bot.polling(non_stop=True)
