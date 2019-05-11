import logging

logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', level=logging.DEBUG)

class Log:

    def debug(self, message):
        logging.debug(message)

    def info(self, message):
        logging.info(message)

    def warn(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)


LOG = Log()