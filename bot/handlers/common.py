import logging

from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)


def handle_dispatcher(dispatcher):
    dispatcher.add_handler(ping())
    dispatcher.add_error_handler(error)


def error(a, b, c):
    logger.error('Error %s %s "%s"' % a, b, c)


def ping():
    def handle(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="pong")

    return CommandHandler('ping', handle)


