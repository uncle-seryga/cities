import telebot
from service import Config

bot = telebot.Telebot(Config().config('bot_api_key'))