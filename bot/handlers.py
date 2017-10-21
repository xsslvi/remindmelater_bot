import logging

from telegram.ext import CommandHandler

logger = logging.getLogger(__name__)


def error():
    logger.error('Error "%s"' % error)


def test():
    text = ""

    def handle(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="It's running")

    return CommandHandler('test', handle)


def help():
    def handle(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="I need somebody")

    return CommandHandler('help', handle)
