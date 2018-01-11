import logging
import os

from telegram.ext import Updater
from telegram.error import InvalidToken

from handlers import test, help, error

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s')

logger = logging.getLogger('bot')


def main():
    try:
        token = os.environ['TELEGRAM_API_TOKEN']
        updater = Updater(token)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(test())
        dispatcher.add_handler(help())
        dispatcher.add_error_handler(error)

        updater.start_polling()
    except KeyError:
        logger.error('TELEGRAM_API_TOKEN variable is not specified')
    except InvalidToken:
        logger.error('Invalid api token')


if __name__ == '__main__':
    main()
