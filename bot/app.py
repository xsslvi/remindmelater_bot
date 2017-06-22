import logging
import os

from telegram.ext import Updater

from handlers import test, help

logging.basicConfig(filename='/logs/bot.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    file = open('/store/' + os.environ['TOKEN_FILE_NAME'], 'r')
    # FIXME: dirty hack
    token = file.read().strip('\n')
    file.close()

    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(test())
    dispatcher.add_handler(help())

    updater.start_polling()

if __name__ == '__main__':
    main()
