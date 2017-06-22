from telegram.ext import CommandHandler


def test():
    text = ""

    def handle(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="It's running")

    return CommandHandler('test', handle)


def help():
    def handle(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="I need somebody")

    return CommandHandler('help', handle)
