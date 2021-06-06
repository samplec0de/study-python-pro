import logging
import datetime

logging.basicConfig(filename='app.log', level=logging.WARNING)
# DEBUG, INFO, WARNING, ERROR, CRITICAL
logger = logging.getLogger("Test")
logger.info('Today is %s', datetime.datetime.now())
logger.error('Лифт не работает')
logger.warning('Сегодня плохая погода')
logger.debug('version=1.0')
logger.critical('crit')
