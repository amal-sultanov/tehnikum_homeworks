import telebot

import buttons
import database

bot = telebot.TeleBot('7934834183:AAEyNjCmZD741QGgvP6Fm-sFi0b6NCuofxU')


@bot.message_handler(commands=['start'])
def start(message):
    if database.is_user_registered(message.from_user.id):
        bot.send_message(message.from_user.id,
                         f'Welcome, @{message.from_user.username}!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.from_user.id, 'Choose from menu:',
                         reply_markup=buttons.show_main_menu(
                             database.get_available_products()))
    else:
        bot.send_message(message.from_user.id,
                         'Hi, you need to register.\n'
                         'Enter your name:',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


@bot.message_handler(content_types=['text'])
def get_name(message):
    user_name = message.text
    bot.send_message(message.from_user.id,
                     'Awesome, now send me your phone number:',
                     reply_markup=buttons.send_number_button())
    bot.register_next_step_handler(message, get_number, user_name)


def get_number(message, user_name):
    if message.contact:
        user_number = message.contact.phone_number
        database.register_user(message.from_user.id, user_name, user_number)
        bot.send_message(message.from_user.id,
                         'You were successfully registered!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.from_user.id,
                         'Send contact using button or paper clip')
        bot.register_next_step_handler(message, get_number, user_name)


bot.polling(non_stop=True)
