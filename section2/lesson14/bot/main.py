import telebot

import keyboards

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.from_user.id,
                     f'Hello, @{message.from_user.username}!',
                     reply_markup=keyboards.menu())


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.title() == 'Wikipedia':
        bot.send_message(message.from_user.id, 'Enter a word',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, search_wiki_info)
    elif message.text.title() == 'Translator':
        bot.send_message(message.from_user.id,
                         'Enter a word to translate: ',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, translate)
    else:
        bot.send_message(message.from_user.id,
                         'Something went wrong, enter /start')
    # bot.send_message(message.from_user.id, 'Wanna talk?')


def search_wiki_info(message):
    if message.text.title() == 'Stalin':
        bot.send_message(message.from_user.id,
                         'https://en.wikipedia.org/wiki/Joseph_Stalin')
        bot.register_next_step_handler(message, text)
    elif message.text.title() == 'Escobar':
        bot.send_message(message.from_user.id,
                         'https://ru.wikipedia.org/wiki/Эскобар,_Пабло')
        bot.register_next_step_handler(message, text)
    else:
        bot.send_message(message.from_user.id, 'No info')


def translate(message):
    if message.text == 'pen':
        bot.send_message(message.from_user.id, 'ручка')
        bot.register_next_step_handler(message, text)
    elif message.text == 'laptop':
        bot.send_message(message.from_user.id, 'ноутбук')
        bot.register_next_step_handler(message, text)
    else:
        bot.send_message(message.from_user.id, 'No translation')


bot.polling(non_stop=True)
