# бот со 2 урока из плейлиста (Телеграм бот на Python / #2 – Базовые концепции создания бота)
import webbrowser

import telebot

bot = telebot.TeleBot('')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.from_user.id,
                     f'Привет, {message.from_user.first_name} '
                     f'{message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.from_user.id,
                     '<b>Help</b> <em><u>information</u></em>',
                     parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id,
                         f'Привет, {message.from_user.first_name} '
                         f'{message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)
