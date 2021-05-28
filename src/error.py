class Error(Exception):
    def __init__(self):
        pass

class CommandError(Error):

    def __init__(self,message):
        self.message = message
