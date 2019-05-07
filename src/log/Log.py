import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

class Log:

    def info(self, message):
        logging.info(message)

    def warn(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)


LOG = Log()