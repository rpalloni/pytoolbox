import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug('hello')  # Module-level function

logger = logging.getLogger(__name__) # instantiate logger object
logger.debug('hello')   # Logger's method


logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')


logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')

name = 'John'
logging.error(f'{name} raised an error')


a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

try:
  c = a / b
except Exception as e:
    logging.error("Short msg:"+str(e)) # exception short message
    logging.error("Traceback:", exc_info=True) # full traceback

# dedicated classes
logger = logging.getLogger(__name__)
logger.warning('This is a warning')

# handler send log messages to configured destinations
c_handler = logging.StreamHandler() # send to std.out
f_handler = logging.FileHandler('log.txt') # send to file
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

# import a log config file
import logging.config

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message using log configuration')
