class ServerNotFound(Exception):
    def __str__(self):
        return "[ERROR]: Couldn't listen server port."
        
class SomethingWentWrong(Exception):
    def __str__(self):
        return '[ERROR]: Something went wrong.'
