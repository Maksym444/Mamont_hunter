import telebot
import time
import json
from datetime import date
from telebot import types
from datetime import datetime

import authy
import databaseInput
import databaseOutput
import tableCreate
import markup_k


bot = telebot.TeleBot(authy.Token)
today = date.today()


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == '/start':
        userId = (message.from_user.id)
        tableCreate.table(userId)
        bot.send_sticker(message.chat.id, 'CAADAgAD7g4AAkKvaQABjt0lnjMy9FAWBA')
        bot.send_message(message.chat.id, "Добро пожаловать охотник " + message.from_user.first_name + "! Колличество убитых тобой мамонтов перевалило за сотни, но со мной, ты не забудешь ни одного из них! Если тебе нужна помощь, набери команду /help")
        bot.send_message(message.chat.id, "Каждый день (кроме выходных), вечером (18:20), я буду спрашивать тебя о твоих охотничьих успехах!")
        # send_w(message)
        count(message)
    elif message.text == '/help':
        bot.reply_to(message,
                     "Каждый день вечером, я буду спрашивать тебя о твоих охотничьих успехах! \n Пиши мне - 'сколько', и я скажу сколько ты заработала за месяц!")
    elif message.text =='/menu':
        send_w(message)
    else:
        bot.send_message(message.chat.id, 'Стадо мамонтов в замешательстве от такой команды')
        bot.send_sticker(message.chat.id, 'CAADAgAD7g4AAkKvaQABjt0lnjMy9FAWBA')

@bot.message_handler(func=lambda message:True)
def check_1(message):
        userId = (message.from_user.id)
        msg = bot.send_message(message.chat.id, "Щас скажу!", time.sleep(0.4))
        bot.send_message(message.chat.id, "Подожди.... считаю!", time.sleep(1.4))
        bot.send_message(message.chat.id, 'За ' + month + ' ты наохотила ' + databaseOutput.rez(userId) + " мамонтейных денежных символов!", time.sleep(1.4))
        bot.send_sticker(message.chat.id, 'CAADAgADLVQAAp7OCwAB3ByKGvkbQr8WBA')

# Модуль для кнопок вне времени
def send_w(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row('Записать мамонтов', 'Узнать колл/ мамонтов')
    msg = bot.reply_to(message, "Каждый день (кроме выходных), вечером (18:10), я буду спрашивать тебя о твоих охотничьих успехах!", reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)

def process_step(message):
    chat_id = message.chat.id
    if message.text == 'Записать мамонтов':
        bot.register_next_step_handler(message, callback = databaseInput.askAge)
    elif message.text == 'Узнать колл/ мамонтов':
        check_1(message)

# Модуль для вопросов по времени
def key():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Охота была удачной!", callback_data="true"),
            types.InlineKeyboardButton("Мамонт был быстрым(", callback_data="false"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "true":
       msg = bot.send_message(call.from_user.id, "И сколько Охотник, Поймал?", time.sleep(0.4))
       bot.send_sticker(call.from_user.id, 'CAADAgAD7g4AAkKvaQABjt0lnjMy9FAWBA', time.sleep(1.4))
       bot.send_message(call.from_user.id, "Или хотя бы...", time.sleep(1.4))
       bot.send_sticker(call.from_user.id, 'CAADAgAEDwACQq9pAAFKOJfjP5SH2RYE', time.sleep(1.4))
       bot.register_next_step_handler(msg, callback=databaseInput.askAge)
    elif call.data == "false":
        bot.send_message(call.from_user.id, "В следующий раз повезет!")

@bot.message_handler(func=lambda message:True)
def message_handler(message):
    bot.send_message(message.chat.id, "Поймала что то сегодня?", reply_markup=key())

# Модуль с запуском по времени

today = date.today()
mydate= datetime.now()
wd = date.weekday(today) #дни начинаються с 0, понедельник
days= ['понедельник', "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
months= ['0_month','январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
month=(months[mydate.month])


def count (message):
    while True:
        if (wd == 0,1,2,3,4):
            # chat_id = 172608373
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            time.sleep(60)
            if current_time == "15:11":
                message_handler(message)
            else:
                pass

try:
    bot.polling(none_stop=True, interval=0, timeout=10000)
except Exception as e:
    time.sleep(10)

