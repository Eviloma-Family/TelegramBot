import os
import telebot
from telebot import types
from dotenv import load_dotenv
from main_page import *
from site_redirection import *

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.from_user.id
    for i in range(1000):
            try:
                bot.delete_message(chat_id, message.id-i)
            except:
                main_page(bot, chat_id)
                break
    
@bot.message_handler(content_types=["text"])
def textMessage(message):
    chat_id = message.from_user.id
    
    if message.text == "Зв’язати Telegram аккаунт із сайтом Family Dashboard 🔐":
        for i in range(1000):
            try:
                bot.delete_message(chat_id, message.id-i)
            except:
                site_registration(bot, chat_id)
                break
            
    if message.text == "Головне Меню 🏠":
        for i in range(1000):
            try:
                bot.delete_message(chat_id, message.id-i)
            except:
                main_page(bot, chat_id)
                break
    
    if message.text == "Перейти на сайт Family Dashboard 🌐":
        for i in range(1000):
            try:
                bot.delete_message(chat_id, message.id-i)
            except:
                site_redirection(bot, chat_id)
                break

bot.polling(none_stop=True)
    