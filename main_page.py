import telebot
from telebot import types

def main_page(bot, chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
    itembtn1 = types.KeyboardButton("Зв’язати Telegram аккаунт із сайтом Family Dashboard 🔐")
    itembtn2 = types.KeyboardButton("Перейти на сайт Family Dashboard 🌐")
    markup.add(itembtn1, itembtn2)
    bot.send_message(chat_id, "ГОЛОВНЕ МЕНЮ:", reply_markup=markup)