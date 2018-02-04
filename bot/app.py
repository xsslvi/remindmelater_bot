import os
from datetime import datetime
from logging import basicConfig, getLogger, StreamHandler, DEBUG, INFO
from logging.handlers import TimedRotatingFileHandler
from telegram.error import InvalidToken

from bot import Bot

if os.environ['ENVIRONMENT'] == 'prod':
    logger_handler = TimedRotatingFileHandler(datetime.now().strftime("%Y-%m-%d"), when="D")
    level = INFO
else:
    logger_handler = StreamHandler()
    level = DEBUG

basicConfig(level=level, datefmt="%Y-%m-%d %H:%M:%S", format='%(asctime)s - %(levelname)s: %(message)s',
            handlers=[logger_handler])

logger = getLogger('bot')


def main():
    try:
        token = os.environ['TELEGRAM_API_TOKEN']
        bot = Bot(token)
        bot.run()
        logger.info('Bot is started')
    except KeyError:
        logger.error('TELEGRAM_API_TOKEN variable is not specified')
    except InvalidToken:
        logger.error('Invalid api token')


if __name__ == '__main__':
    main()
