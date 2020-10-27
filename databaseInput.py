import pymysql
import telebot
from contextlib import closing
from pymysql.cursors import DictCursor
from datetime import date
from datetime import datetime
import time


today = date.today()
mydate= datetime.now()
wd = date.weekday(today) #дни начинаються с 0, понедельник
days= ['понедельник', "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
months= ['0_month','январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
month=(months[mydate.month])

import authy
bot = telebot.TeleBot(authy.Token)
connection = pymysql.connect(host='localhost', user='root', password='', db='ohota', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
print("connection complete")

def askAge(mes):
    chat_id = mes.chat.id
    text = mes.text
    user_id = str (mes.from_user.id)
    user_name = str (mes.from_user.username)
    userId = (mes.from_user.id)
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Это конечно неплохо, но введи цифрами пожалуйста!')
    else:
        connection.connect()  # Подключение
        with connection.cursor() as cursor:
                print(userId)
                query = ("INSERT INTO `%s` (tg_id, user_name, Quantity, Day, Month, Year) VALUES (%s, %s, %s, %s, %s, %s)")
                cursor.execute(query, (userId, user_id, user_name, text, today.day, today.month, today.year))
                connection.commit()
                print(connection.cursor().rowcount, "record inserted.")
                cursor.close()
                connection.close()
        if wd>=4:
            bot.send_message(chat_id, 'Ого целых ' + text + ' это же мамонт. А завтра ты сможешь отдохнуть потому что выходной')
            bot.send_sticker(chat_id, 'CAADAgAEDwACQq9pAAFKOJfjP5SH2RYE', time.sleep(1.4))
            bot.send_sticker(chat_id, 'CAADAgAD7g4AAkKvaQABjt0lnjMy9FAWBA', time.sleep(1.4))

        else:
            bot.send_sticker(chat_id, 'CAADAgAEDwACQq9pAAFKOJfjP5SH2RYE', time.sleep(1.4))
            bot.send_message(chat_id, 'Ого целых ' + text + ' это же мамонт. А завтра будет ' + days[wd+1] + " ещё более удачный день для охоты!!!")

