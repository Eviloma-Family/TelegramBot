import telebot
from telebot import types
import random
import os
from threading import *
import time
import requests
from supabase import telegram_temporary_code
from main_page import main_page
    
def site_registration(bot, chat_id):
    temporary_code = random.randint(0,999999)
    temporary_code = f'{"0" * (6 - len(str(temporary_code)))}{str(temporary_code)}'
    status_code = telegram_temporary_code(temporary_code, chat_id)
    if (status_code != 0):
        bad_request(bot, chat_id, status_code)
        print(status_code)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
        itembtn1 = types.KeyboardButton("Головне Меню 🏠")
        markup.add(itembtn1)
        bot.send_message(chat_id, "Перейдіть за посиланням для прив’язки телеграм аккаунта.\n"
                        +"Ваш тимчасовий код для прив’язки - " + temporary_code, reply_markup=markup)
        markup2 = types.InlineKeyboardMarkup()
        url = os.getenv("SITEURL") + "link?code=" + temporary_code
        itembtn2 = types.InlineKeyboardButton("↘️ Перейти за посиланням ↙️", url = url)
        markup2.add(itembtn2)
        bot.send_message(chat_id, url, reply_markup=markup2)
    
def bad_request(bot, chat_id, status_code):
    markup = types.InlineKeyboardMarkup()
    reportbtn = types.InlineKeyboardButton("🔊 Повідомити про проблему 🔊", callback_data = "error request")
    markup.add(reportbtn)
    bot.send_message(chat_id, "Отакої, щось зламалось😳\n"+
                     "Повідомте про проблему адміністрацію🤡", reply_markup=markup)
    markup2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
    itembtn1 = types.KeyboardButton("Головне Меню 🏠")
    markup2.add(itembtn1)
    bot.send_message(chat_id, "Скористуйтеся цією функцією пізніше, зараз ви можете повернутися до Головного Меню 😅", reply_markup=markup2)
    
    
    @bot.callback_query_handler(lambda query: query.data == "error request")
    def error_request(query):
        admin_id = os.getenv("ADMIN_ID")
        bot.send_message(chat_id, "✅ Повідомлення проблеми надіслано адміністратору", reply_to_message_id = query.message.id)
        bot.send_message(admin_id, "⁉️ Баг репорт від користувача "+ str(chat_id) +"\n"+ status_code)
        
def site_redirection(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
    itembtn1 = types.KeyboardButton("Головне Меню 🏠")
    markup.add(itembtn1)
    bot.send_message(chat_id, "Перехід на сайт можливий за посиланням:", reply_markup=markup)
    markup2 = types.InlineKeyboardMarkup()
    url = os.getenv("SITEURL")
    itembtn = types.InlineKeyboardButton("↘️ Перейти за посиланням ↙️", url = url)
    markup2.add(itembtn)
    bot.send_message(chat_id, url, reply_markup=markup2)
    
        