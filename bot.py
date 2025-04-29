import telebot
from telebot import types

API_TOKEN = '5145023087:AAElLJz71P6JG1BfVAGnILkv44fWiPANU7A'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['MesButton'])
def send_menu(message):
    # Создаем клавиатуру для кнопок в сообщении
    markup = types.InlineKeyboardMarkup()

    # Добавляем кнопки
    item1 = types.InlineKeyboardButton('Дом 🏠', callback_data='button1')
    item2 = types.InlineKeyboardButton('Мастерская ⚙️', callback_data='button2')

    # Добавляем кнопки на клавиатуру
    markup.add(item1, item2)

    # Отправляем сообщение с 
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(commands=['MenButton'])
def send_menu(message):
    # Создаем клавиатуру для кнопок в меню
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    # Добавляем кнопки
    item1 = types.KeyboardButton('Главное меню 🏠')
    item2 = types.KeyboardButton('Настройки ⚙️')

    # Добавляем кнопки на клавиатуру
    markup.add(item1, item2)

    # Отправляем сообщение с меню
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # Обработка нажатий на инлайн-кнопки
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, "Вы в доме 🏠")
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, "Вы в мастерской ⚙️")

@bot.message_handler(func=lambda message: True)
def handle_option(message):
    if message.text == 'Главное меню 🏠':
        bot.send_message(message.chat.id, "Вы в главном меню.")
    elif message.text == 'Настройки ⚙️':
        bot.send_message(message.chat.id, "Вы в настройках.")

bot.polling()
