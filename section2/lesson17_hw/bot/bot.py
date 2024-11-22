import telebot

import database
import keyboards

bot = telebot.TeleBot('')
user_data = {}


@bot.message_handler(commands=['start'])
def start(message):
    if database.is_user_registered(message.from_user.id):
        language = database.get_language(message.from_user.id)

        if language == 'ru':
            bot.send_message(message.from_user.id,
                             f'Добро пожаловать, @{message.from_user.username}!',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        elif language == 'uz':
            bot.send_message(message.from_user.id,
                             f'Xush kelibsiz, @{message.from_user.username}!',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        else:
            bot.send_message(message.from_user.id,
                             '🇷🇺Ваш язык не установлен, выберите язык снова // 🇺🇿Tilni yana tanlang',
                             reply_markup=keyboards.send_language_buttons())
    else:
        bot.send_message(message.from_user.id,
                         '🇷🇺Выберите язык \\ 🇺🇿Tilni tanlang',
                         reply_markup=keyboards.send_language_buttons())


@bot.callback_query_handler(lambda call: call.data in ('ru', 'uz'))
def select_language(call):
    language = call.data
    user_data[call.from_user.id] = {'language': language}

    if language == 'ru':
        bot.send_message(call.from_user.id, 'Введите ваше имя',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif language == 'uz':
        bot.send_message(call.from_user.id, 'Ismingizni kiriting',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(call.message, get_name)


@bot.message_handler(content_types=['text'])
def get_name(message):
    user_name = message.text
    language = user_data[message.from_user.id]['language']

    if language == 'ru':
        bot.send_message(message.from_user.id, 'Отправьте ваш номер телефона',
                         reply_markup=keyboards.send_number_button(
                             'Отправить номер'))
    elif language == 'uz':
        bot.send_message(message.from_user.id,
                         'Telefon raqamingizni yuboring',
                         reply_markup=keyboards.send_number_button(
                             'Raqamni jo\'natish'))
    bot.register_next_step_handler(message, get_number, user_name, language)


def get_number(message, user_name, language):
    if message.contact:
        user_number = message.contact.phone_number

        if language == 'ru':
            bot.send_message(message.from_user.id,
                             'Отправьте ваше местоположение',
                             reply_markup=keyboards.send_location_button(
                                 'Отправить местоположение'))
        elif language == 'uz':
            bot.send_message(message.from_user.id,
                             'Manzilingizni jo\'nating:',
                             reply_markup=keyboards.send_location_button(
                                 'Manzilni jo\'natish'))
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number, language)
    else:
        if language == 'ru':
            bot.send_message(message.from_user.id,
                             'Отправьте номер через кнопку или скрепку')
        elif language == 'uz':
            bot.send_message(message.from_user.id,
                             'Raqamni tugma yoki qog\'oz tugmachasi orqali yuboring')
        bot.register_next_step_handler(message, get_number, user_name,
                                       language)


def get_location(message, user_name, user_number, language):
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        user_data.pop(message.from_user.id)
        database.register_user(message.from_user.id, user_name,
                               user_number, latitude, longitude, language)

        if language == 'ru':
            bot.send_message(message.from_user.id,
                             'Вы успешно зарегистрированы!',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        elif language == 'uz':
            bot.send_message(message.from_user.id,
                             'Siz muvaffaqiyatli ro\'yxatdan o\'tdingiz!',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        if language == 'ru':
            bot.send_message(message.from_user.id,
                             'Отправьте местоположение через кнопку или скрепку')
        elif language == 'uz':
            bot.send_message(message.from_user.id,
                             'Manzilingizni tugma yoki qog\'oz tugmachasi orqali jo\'nating')
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number, language)


bot.polling(non_stop=True)
