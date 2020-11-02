import pymysql
import telebot
from contextlib import closing
from pymysql.cursors import DictCursor
from datetime import date
from datetime import datetime
import time

import authy
bot = telebot.TeleBot(authy.Token)
connection = pymysql.connect(host='localhost', user='root', password='', db='ohota', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

def table(userId):
    with connection.cursor() as cursor:
     cursor.execute ("CREATE TABLE IF NOT EXISTS `%s` (id INT AUTO_INCREMENT PRIMARY KEY, tg_id INT, user_name text, Quantity INT, Day INT, Month INT, Year INT)", userId)
     connection.commit()
     cursor.close()
     connection.close()
