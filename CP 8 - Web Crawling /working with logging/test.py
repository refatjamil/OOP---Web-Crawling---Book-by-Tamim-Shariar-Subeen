import logging

logging.basicConfig(filename='test.log', filemode='w', level=logging.DEBUG)

logging.debug('This is debug log')
logging.info('This is debug log')
logging.warning('This is debug log')
logging.error('This is debug log')
logging.critical('This is debug log')