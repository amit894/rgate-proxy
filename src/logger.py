import logging
from file import file_write

class Logger():
    def __init__():
        pass

    log_file="../logs/rgate.log"
    log_level=logging.INFO

    @staticmethod
    def write(status_code,response_time):
        print(status_code,response_time)
        file_write(Logger.log_file,str(status_code)+"-"+str(response_time))
        #logging.basicConfig(level=Logger.log_level, filename=Logger.log_file,format="%(response_code)s %(response_time)s")
