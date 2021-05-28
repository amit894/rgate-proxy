import logging

class Logger():
    def __init__():
        pass

    log_file="../logs/rgate.log"
    log_level=logging.INFO

    @staticmethod
    def write():
        logging.basicConfig(level=Logger.log_level, filename=Logger.log_file)
