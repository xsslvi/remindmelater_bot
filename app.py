import os

from telegram.ext import Updater, CommandHandler

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

print(os.environ['TOKEN_FILE_NAME'])
file = open('/store/' + os.environ['TOKEN_FILE_NAME'], 'r')
token = file.read()
file.close()

updater = Updater(token)
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="It's running")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

