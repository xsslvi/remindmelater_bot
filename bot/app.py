import logging
import os

from telegram.ext import Updater

from handlers import test_handler, help_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

file = open('/store/' + os.environ['TOKEN_FILE_NAME'], 'r')
# FIXME: dirty hack
token = file.read().strip('\n')
file.close()

updater = Updater(token)
dispatcher = updater.dispatcher

dispatcher.add_handler(test_handler())
dispatcher.add_handler(help_handler())

updater.start_polling()

