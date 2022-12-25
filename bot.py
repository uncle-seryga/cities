import telebot

import game
import register
from service import Config

bot = telebot.TeleBot("5727998641:AAGmixf7PBRDZ3nStxTQJx30PzP8e4BGZiA") #Config().config('bot_api_key')


@bot.message_handler(content_types=['text'])
def action(message: telebot.types.Message):
    if message.text == '/start':

        register_object = register.Register(message.from_user.first_name, message.chat.id)
        if not register_object.check_if_register():
            print(register_object.message)
            bot.send_message(message.chat.id, register_object.message)
        else:
            print(register_object.message)
            bot.send_message(message.chat.id, register_object.message)

bot.polling()
