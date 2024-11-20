import telebot

import database
import keyboards

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    if database.is_user_registered(message.from_user.id):
        bot.send_message(message.from_user.id,
                         f'Welcome, @{message.from_user.username}!')
    else:
        bot.send_message(message.from_user.id,
                         'Hi, you need to register.\n'
                         'Enter your name:',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id,
                     '/start - to start the bot\n'
                     '/help - to see the information about commands\n',
                     reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'])
def get_name(message):
    user_name = message.text
    bot.send_message(message.from_user.id,
                     'Awesome, now send me your phone number:',
                     reply_markup=keyboards.send_number_button())
    bot.register_next_step_handler(message, get_number, user_name)


def get_number(message, user_name):
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(message.from_user.id,
                         'Good, now send me your location:',
                         reply_markup=keyboards.send_location_button())
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number)
    else:
        bot.send_message(message.from_user.id,
                         'Send contact using button or paper clip')
        bot.register_next_step_handler(message, get_number, user_name)


def get_location(message, user_name, user_number):
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        database.register_user(message.from_user.id, user_name,
                               user_number, latitude, longitude)
        bot.send_message(message.from_user.id,
                         'You were successfully registered!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.from_user.id,
                         'Send location using button or paper clip')
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number)


bot.polling(non_stop=True)
