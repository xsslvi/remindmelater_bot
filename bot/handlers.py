from telegram.ext import CommandHandler


def test_handler():
    def test(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="It's running")

    return CommandHandler('test', test)


def help_handler():
    def help(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="I need somebody")

    return CommandHandler('help', help)
