import time
from datetime import date
from datetime import datetime
import telebot
from telebot import types
import pymysql

import authy
import databaseOutput
import tableCreate

bot = telebot.TeleBot(authy.Token)

connection = pymysql.connect(host='localhost', user='root', password='', db='ohota', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == '/start':
        userId = (message.from_user.id)
        tableCreate.table(userId)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJF4V-fz0YeZcDLF1cYK43bH648zgULAAL3IwAC2NjhAAErep5KrSRC-x4E')
        bot.send_message(message.chat.id, "Добро пожаловать охотник " + message.from_user.first_name + "! Колличество убитых тобой мамонтов перевалило за сотни, но со мной, ты не забудешь ни одного из них! \n Воспользуйся кнопками для записи и вывода мамонтейных символов!")
        send_w(message)
        count(message)
    else:
        bot.send_message(message.chat.id, 'Стадо мамонтов в замешательстве от такой команды.')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJF5F-f1NWSI55IFZ7GIMPnGs_U5KQ1AAICJAAC2NjhAAF8cWMQlFx9fB4E')
        return

@bot.message_handler(func=lambda message:True)
def check_1(message):
    try:
        userId = (message.from_user.id)
        if databaseOutput.rez(userId):
            bot.send_message(message.chat.id, "Щас скажу!", time.sleep(0.4))
            bot.send_message(message.chat.id, "Подожди.... считаю!", time.sleep(0.4))
            bot.send_message(message.chat.id, 'За ' + month + ' ты наохотила ' + databaseOutput.rez(userId) + " мамонтейных денежных символов!", time.sleep(0.4))
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJF9l-f4x6jiH82p2RjRIHFble13evOAAIFJAAC2NjhAAEm2zGCPZKwrx4E')
            bot.register_next_step_handler(message, process_step)
        else:
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJF6l-f1TzFWZDOz_W48sVhTKbFFdQQAAL2IwAC2NjhAAF8tHGAnXbFGB4E')
            bot.send_message(message.chat.id, '... но ты пока ещё ничего не наохотил!')
    except Exception as e:
        bot.reply_to(message, 'check_1')

# Модуль для кнопок вне времени
def send_w(message):
    try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('Записать мамонтейные символы', 'Вывести мамонтейные символы')
        msg = bot.reply_to(message, "Каждый день (кроме выходных), вечером (18:10), я буду спрашивать тебя о твоих охотничьих успехах! Следуй инструкциям! Жми команды 'Записать мамонтейные символы' что бы записать информацию и 'Вывести мамонтейные символы' что бы вывести информацию!", reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    except Exception as e:
        bot.reply_to(message, 'send_w')

def process_step(message):
    try:
        chat_id = message.chat.id
        if message.text == 'Записать мамонтейные символы':
            bot.send_message(chat_id, "И сколько Охотник, Поймал?")
            bot.register_next_step_handler(message,askAge)
        elif message.text == 'Вывести мамонтейные символы':
            check_1(message)
        else:
            msg=bot.send_message(chat_id," Охотник, стадо в замешательстве, они застряли в каньйоне непонятных комманд")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJF7V-f3tsv3w97iacryA1D8QPRECfrAAL7IwAC2NjhAAFnsL5BNKi8bh4E')
            bot.register_next_step_handler(msg, process_step)
            return
    except Exception as e:
        bot.reply_to(message, 'process_step')

# Модуль для вопросов по времени
def key():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Охота была удачной!", callback_data="true"),
            types.InlineKeyboardButton("Мамонт был быстрым(", callback_data="false"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == "true":
           msg = bot.send_message(call.from_user.id, "И сколько Охотник, Поймал?", time.sleep(0.4))
           bot.register_next_step_handler(msg, askAge)
        elif call.data == "false":
            bot.send_message(call.from_user.id, "Завтра повезет!")
            bot.send_sticker(call.from_user.id,'CAACAgIAAxkBAAJF8F-f33uRd06bYaszwK2fG5GCDZP5AAMkAALY2OEAAWRx10mg82tPHgQ')
    except Exception as e:
        bot.reply_to(call.from_user.id, 'callback_query')

@bot.message_handler(func=lambda message:True)
def message_handler(message):
    try:
        bot.send_message(message.chat.id, "Наохотил, что то сегодня?", reply_markup=key())
    except Exception as e:
        bot.reply_to(message, 'message_handler')

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
            chat_id=message.chat.id
            if (chat_id == 172608373):
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                time.sleep(60)
                if current_time == "09:08":
                    message_handler(message)
                else:
                    pass

def askAge (mes):
    chat_id = mes.chat.id
    text = mes.text
    user_id = str (mes.from_user.id)
    user_name = str (mes.from_user.username)
    userId = (mes.from_user.id)
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Это конечно неплохо, но введи цифрами пожалуйста!')
        bot.register_next_step_handler(msg, askAge)
        return
    else:
        connection.connect()  # Подключение
        with connection.cursor() as cursor:
                query = ("INSERT INTO `%s` (tg_id, user_name, Quantity, Day, Month, Year) VALUES (%s, %s, %s, %s, %s, %s)")
                cursor.execute(query, (userId, user_id, user_name, text, today.day, today.month, today.year))
                connection.commit()
                # print(connection.cursor().rowcount, "record inserted.")
                cursor.close()
                connection.close()
        if wd>=4:
            bot.send_message(chat_id, 'Ух ты ' + text + ' это же мамонт. А завтра ты сможешь отдохнуть потому что выходной')
            bot.send_sticker(chat_id, 'CAACAgIAAxkBAAJF81-f4EjN6cmeiUrFdKmtGTuBICepAAIBJAAC2NjhAAGzcjI6o7R5nx4E', time.sleep(0.4))
            bot.register_next_step_handler(mes, process_step)
        else:
            bot.send_message(chat_id, 'Ух ты ' + text + ' это же мамонт. А завтра будет ' + days[wd+1] + " ещё более удачный день для охоты!!!")
            bot.send_sticker(chat_id, 'CAACAgIAAxkBAAJF81-f4EjN6cmeiUrFdKmtGTuBICepAAIBJAAC2NjhAAGzcjI6o7R5nx4E', time.sleep(0.4))
            bot.register_next_step_handler(mes, process_step)

try:
    bot.polling(none_stop=True, interval=0, timeout=100000)
except Exception as e:
    time.sleep(10)

