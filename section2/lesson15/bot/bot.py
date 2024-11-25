import telebot

import buttons
import database

bot = telebot.TeleBot('')
users = {}
admins = {}


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


def get_name(message):
    user_name = message.text
    bot.send_message(message.from_user.id,
                     'Awesome, now send me your phone number:',
                     reply_markup=buttons.send_number_button())
    bot.register_next_step_handler(message, get_number, user_name)


@bot.callback_query_handler(
    lambda call: call.data in ['decrement', 'increment', 'add_to_cart', 'back']
)
def select_quantity(call):
    user_id = call.from_user.id

    if call.data == 'increment':
        bot.edit_message_reply_markup(user_id, call.message.message_id,
                                      reply_markup=buttons.select_quantity(
                                          database.get_product(
                                              users[user_id]['product_name']
                                          )[4],
                                          'increment',
                                          users[user_id]['quantity']
                                      ))
        users[user_id]['quantity'] += 1
    elif call.data == 'decrement':
        bot.edit_message_reply_markup(user_id, call.message.message_id,
                                      reply_markup=buttons.select_quantity(
                                          database.get_product(
                                              users[user_id]['product_name']
                                          )[4],
                                          'decrement',
                                          users[user_id]['quantity']
                                      ))
        users[user_id]['quantity'] -= 1
    elif call.data == 'add_to_cart':
        product_name = database.get_product(users[user_id]['product_name'])[1]
        database.add_to_cart(user_id, product_name, users[user_id]['quantity'])
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(call.from_user.id,
                         'Item was added to cart. Want more?',
                         reply_markup=buttons.show_main_menu(
                             database.get_available_products()))
    elif call.data == 'back':
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(call.message.from_user.id,
                         'Back to menu',
                         reply_markup=buttons.show_main_menu(
                             database.get_available_products()))


@bot.callback_query_handler(
    lambda call: call.data in ['order', 'clear', 'cart']
)
def cart_handler(call):
    user_id = call.message.chat.id
    text = 'Your cart: \n\n'

    if call.data == 'cart':
        user_cart = database.show_cart(user_id)
        total_price = 0.0

        for product in user_cart:
            text += (f'Item: {product[1]}\n'
                     f'Quantity: {product[2]}\n')
            total_price += database.get_price(product[1])[0] * product[2]
        text += f'Total: {round(total_price, 2)} sum'
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, text, reply_markup=buttons.cart_buttons())
    elif call.data == 'clear':
        database.clear_cart(user_id)
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, 'Cart was cleared',
                         reply_markup=buttons.show_main_menu(
                             database.get_available_products()))
    elif call.data == 'order':
        text = text.replace('Your cart:', 'New order')
        user_cart = database.show_cart(user_id)
        total_price = 0.0

        for product in user_cart:
            text += (f'Item: {product[1]}\n'
                     f'Quantity: {product[2]}\n')
            total_price += database.get_price(product[1])[0] * product[2]
        text += f'Total: {round(total_price, 2)} sum\n'
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, 'Send the location (where to deliver)',
                         reply_markup=buttons.send_location_button())
        bot.register_next_step_handler(call.message, get_location, text)


def get_location(message, text):
    user_id = message.from_user.id

    if message.location:
        text += f'Client: @{message.from_user.username}'
        bot.send_message(message.chat.id, text)
        bot.send_location(message.chat.id, latitude=message.location.latitude,
                          longitude=message.location.longitude)
        database.make_order(user_id)
        database.clear_cart(user_id)
        bot.send_message(user_id, 'Your order was accepted',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Select from menu',
                         reply_markup=buttons.show_main_menu(
                             database.get_available_products()))
    else:
        bot.send_message(user_id, 'Send location using button or paper clip')
        bot.register_next_step_handler(message, get_location, text)


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


@bot.callback_query_handler(
    lambda call: int(call.data) in [i[0] for i in database.get_all_products()]
)
def select_product_quantity(call):
    user_id = call.message.chat.id
    product_info = database.get_product(int(call.data))
    bot.delete_message(user_id, message_id=call.message.message_id)
    bot.send_photo(user_id, product_info[-1],
                   f'{product_info[1]}\n\n'
                   f'Description: {product_info[2]}\n'
                   f'Quantity: {product_info[4]}\n'
                   f'Price: {product_info[3]} sum',
                   reply_markup=buttons.select_quantity(product_info[4]))
    users[user_id] = {'product_name': call.data,
                      'quantity': 1}


@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.id == 62828291:
        admin_id = message.from_user.id
        bot.send_message(admin_id, 'Welcome to admin dashboard',
                         reply_markup=buttons.admin_menu())
        bot.register_next_step_handler(message, choice)
    else:
        bot.send_message(message.from_user.id, 'You are not an administrator')


def choice(message):
    admin_id = message.from_user.id

    if message.text == 'Add product':
        bot.send_message(admin_id,
                         'Enter product data in following format:\n\n'
                         'Product name, description, price, quantity, image link\n\n'
                         'Images can be loaded on https://postimages.org, then copy the link',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, add_product)


def add_product(message):
    admin_id = message.from_user.id
    product_attributes = message.text.split(', ')
    database.add_product(product_attributes[0], product_attributes[1],
                         product_attributes[2], product_attributes[3],
                         product_attributes[4])
    bot.send_message(admin_id, 'Done!')


bot.polling(non_stop=True)
