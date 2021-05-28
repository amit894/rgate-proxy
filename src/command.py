import os

class Command():
    def __init__(self):
        pass

    @staticmethod
    def run_command(cmd,args):
        try:
            print(cmd+" "+args)
            result_code=os.system(cmd+" "+args)
            return (result_code)
        except OSError as error :
            print(error)
