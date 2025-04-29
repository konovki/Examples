# Занятие по созданию TelegramBot-а

#### Создаем обработчик команд 
```ruby
import telebot

API_TOKEN = 'Token'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот.")


bot.polling()
```

#### Смотрим на содерижимое message
```ruby
import telebot

API_TOKEN = 'Token'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['info'])
def send_info(message):
    for data in message.__dict__:
        print(data, message.__dict__[data])


bot.polling()

```
#### Обработчик текста 
```ruby
import telebot

API_TOKEN = 'Token'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_option(message):
    bot.reply_to(message, f"Вы сказали: {message.text}")

bot.polling()

```
#### Обрабатываем текст от пользователя
```ruby
import telebot

API_TOKEN = 'Token'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_option(message):
    text = message.text.split(' ')
    if text[0] == 'скажи':
        bot.reply_to(message, f"Вы сказали: {message.text}")
    elif text[0] == 'молчи':
        bot.reply_to(message, f"Вы сказали молчать")
    else:
        pass


bot.polling()

```
#### Учимся отправлять пользователю сообщение в формате кода
```ruby
import telebot

API_TOKEN = 'Token'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['info'])
def send_info(message):
    for data in message.__dict__:
        print(data, message.__dict__[data])

    text = (f'username: {message.from_user.username}\n'
            f'first_name: {message.from_user.first_name}\n'
            f'last_name: {message.from_user.last_name}\n'
            f'id: {message.from_user.id}\n')
    bot.reply_to(message, text)
    code_text = f"```\n{text}\n```"
    id = message.from_user.id
    bot.send_message(id, text=code_text, parse_mode='MarkdownV2')


bot.polling()

```

#### Создание кнопок в сообщении и в меню
```ruby
import telebot
from telebot import types

API_TOKEN = 'Token'
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

    # Отправляем сообщение с меню
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

    # Отправляем сообщение с кнопками
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

```
