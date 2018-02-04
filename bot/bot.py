from telegram.ext import Updater, ConversationHandler
from handlers.conversation import entry_points, states, fallbacks
from handlers.common import ping, error


class Bot:
    def __init__(self, token):
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher
        self.init_handlers()

    def init_handlers(self):
        self.dispatcher.add_handler(ping())
        conversation = ConversationHandler(entry_points(), states(), fallbacks())
        self.dispatcher.add_handler(conversation)
        self.dispatcher.add_error_handler(error)

    def run(self):
        self.updater.start_polling()
