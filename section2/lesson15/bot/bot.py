import telebot

bot = telebot.TeleBot('7934834183:AAEyNjCmZD741QGgvP6Fm-sFi0b6NCuofxU')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Hello')
