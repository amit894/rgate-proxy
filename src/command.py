import os

class Command():
    def __init__(self):
        pass

    @staticmethod
    def run_command(cmd,args):
        try:
            result_code=os.system(cmd+" "+args)
            return (result_code)
        except TypeError as error :
            return error

    def run_command_output(cmd,args):
        try:
            result=os.popen(cmd+" "+args).read()
            return (result)
        except TypeError as error :
            return error
