import telebot
import authy
import json
import pymysql
from datetime import datetime
import re


connection = pymysql.connect(host='localhost', user='root', password='', db='ohota', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

bot = telebot.TeleBot(authy.Token)

mydate= datetime.now()
months= ['0_month','январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
month=mydate.month

def rez (userId):
    connection.connect()
    cur = connection.cursor()
    cur.execute("SELECT sum(Quantity) FROM `%s` where month =%s", (userId, month))
    a = (json.dumps(cur.fetchall(), indent=0, sort_keys=True, default=str))
    nums = re.findall(r'\d+', a)
    nums = [int(i) for i in nums]
    cur.close()
    connection.close()
    return (str(", ".join(repr(e) for e in nums)))




# def rez_last_week ():
#     cur.execute("SELECT sum(Quantity) FROM mamont where day between 1 and 7")
#     return json.dumps(cur.fetchall(),indent=0, sort_keys=True, default=str)
#
# def rez_last_week1 ():
#     cur.execute("SELECT sum(Quantity) FROM mamont where day between 8 and 14")
#     return json.dumps(cur.fetchall(),indent=0, sort_keys=True, default=str)
#
# def rez_last_week2 ():
#     cur.execute("SELECT sum(Quantity) FROM mamont where day between 15 and 21")
#     return json.dumps(cur.fetchall(),indent=0, sort_keys=True, default=str)
#
# def rez_last_week3 ():
#     cur.execute("SELECT sum(Quantity) FROM mamont where day between 21 and 31")
#     return json.dumps(cur.fetchall(),indent=0, sort_keys=True, default=str)

