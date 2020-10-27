# import telebot
# from telebot import types
# import time
#
# API_TOKEN = '810042566:AAFxp0gdDHEhFqSTMeMrHOzk1ztcv2f1bno'
#
# bot = telebot.TeleBot(API_TOKEN)
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     markup.add('1', '2') #Имена кнопок
#     msg = bot.reply_to(message, 'Test text', reply_markup=markup)
#     bot.register_next_step_handler(msg, process_step)
#
# def process_step(message):
#     chat_id = message.chat.id
#     if message.text=='1':
#       bot.send_message(chat_id,'1')
#     else:
#         bot.send_message(chat_id, '2')
#
#
# try:
#     bot.polling(none_stop=True, interval=0, timeout=10000)
# except Exception as e:
#     time.sleep(10)