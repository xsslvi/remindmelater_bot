from enum import Enum

from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import InvertedFilter, Filters


class States(Enum):
    MESSAGE = 1
    TIME = 2


def entry_points():
    def handle_start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text='Just send me a message, and I will ask you to specify remind time')
        return States.MESSAGE

    return [CommandHandler('start', handle_start)]

def


def states():
    def handle_send(bot, update):
        keyboard = ReplyKeyboardMarkup([[KeyboardButton('test1'), KeyboardButton('test2')]], one_time_keyboard=True)
        bot.send_message(chat_id=update.message.chat_id,
                         text='Now specify remind time please', reply_markup=keyboard)
        return States.TIME

    send = MessageHandler(InvertedFilter(Filters.command), handle_send)

    def handle_display(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text='Your reminders: ... (Not implemented yet)')

    display = CommandHandler('show', handle_display)

    def handle_remind(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text='Thanks, reminder is set! (Not implemented yet)')
        return States.MESSAGE

    remind = MessageHandler(InvertedFilter(Filters.command), handle_remind)

    return {States.MESSAGE: [send, display], States.TIME: [remind]}


def fallbacks():
    def handle_end(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text='Ciao')

    return [CommandHandler('end', handle_end)]
