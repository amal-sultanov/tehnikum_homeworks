import telebot

bot = telebot.TeleBot('7882237645:AAEogmFBpCAQfl5uocSz9B41A9eo4Znwrx4')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
                     f'Hello, @{message.from_user.username}!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, '/start - to start the bot\n'
                                           '/help - to see the manual\n'
                                           'all for now...')


bot.polling(non_stop=True)
