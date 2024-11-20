import telebot

bot = telebot.TeleBot('7925099440:AAH8b_GkXZGCR-ISVne1TMpCNTF0i914ouw')


@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.from_user.id,
                     f'Hello, @{message.from_user.username}!')


bot.polling(non_stop=True)
