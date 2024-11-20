import requests
import telebot
from telebot import types

bot = telebot.TeleBot('')
components = {'target_currency': '', 'current_currency': '', 'amount': 0}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
                     f'Hello, @{message.from_user.username}!\n'
                     f'What would you like to do?',
                     reply_markup=show_menu())


@bot.message_handler(content_types=['text'])
def select_operation(message):
    if message.text == 'Convert currency':
        bot.send_message(message.from_user.id,
                         'What is your desirable currency?',
                         reply_markup=get_currencies())
        bot.register_next_step_handler(message, select_target_currency)
    elif message.text == 'Available currencies':
        bot.send_message(message.from_user.id,
                         'Here is a list of currencies available:',
                         reply_markup=get_currencies())
        bot.register_next_step_handler(message, handle_currencies)
    else:
        bot.send_message(message.from_user.id, 'Wrong operation!')


def show_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Convert currency')
    button2 = types.KeyboardButton('Available currencies')
    keyboard.add(button1, button2)

    return keyboard


def get_currencies():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    data = requests.get('https://nbu.uz/en/exchange-rates/json/').json()
    buttons = [types.KeyboardButton('Back')]

    for i in data:
        button = types.KeyboardButton(f'{i["title"]}')
        buttons.append(button)

    keyboard.add(*buttons)
    return keyboard


def get_currencies_titles():
    data = requests.get('https://nbu.uz/en/exchange-rates/json/').json()
    titles = []

    for i in data:
        titles.append(i['title'])

    return titles


def get_currency_by_title(title, data):
    for i in data:
        if i['title'] == title:
            return i
    return None


def select_target_currency(message):
    components['target_currency'] = message.text

    if message.text == 'Back':
        bot.send_message(message.from_user.id, 'Select what you want:',
                         reply_markup=show_menu())
    else:
        bot.send_message(message.from_user.id,
                         'What currency do you want to exchange for it?',
                         reply_markup=get_currencies())
        bot.register_next_step_handler(message, select_current_currency)


def select_current_currency(message):
    components['current_currency'] = message.text
    bot.send_message(message.from_user.id,
                     f'Enter the amount of {components['target_currency']}'
                     f' you want to have:',
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, calculate_rate)


def calculate_rate(message):
    components['amount'] = int(message.text)
    data = requests.get('https://nbu.uz/en/exchange-rates/json/').json()
    current_currency_data = get_currency_by_title(
        components['current_currency'],
        data)
    target_currency_data = get_currency_by_title(
        components['target_currency'],
        data)
    cb_price1 = float(current_currency_data['cb_price'])
    cb_price2 = float(target_currency_data['cb_price'])
    code1, code2 = current_currency_data['code'], target_currency_data['code']

    final_amount = '%.2f' % (components['amount'] * cb_price2 / cb_price1)
    bot.send_message(message.from_user.id,
                     f'You need {final_amount} {code1} '
                     f'to have {components['amount']} {code2}')


def handle_currencies(message):
    data = requests.get('https://nbu.uz/en/exchange-rates/json/').json()
    result = ''

    if message.text == 'Back':
        bot.send_message(message.from_user.id, 'Select what you want:',
                         reply_markup=show_menu())
    elif message.text in get_currencies_titles():
        for i in data:
            if i['title'] == message.text:
                result += f'{i["title"]} - {i["cb_price"]} (Central Bank Price)'
        bot.send_message(message.from_user.id, result,
                         reply_markup=telebot.types.ReplyKeyboardRemove())


bot.polling(non_stop=True)
