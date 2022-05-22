NOT_FOUND = 404
ESTABLISHED = 200

class ConnectionEstablished:
    def __str__(self):
        return 'Status Code: ' + str(self.__status) + ' ' + 'HTTP/HTTPS'

    def __init__(self, ping):
        if ping is None:
            ping = False

        self.__ping = ping
        self.__status = NOT_FOUND
        self.__time = 1

    @property
    def ping(self):
            return self.__ping
        
    @ping.setter
    def ping(self,value):
        self.__ping = value
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,value):
        self.__data = value
    
    @property
    def status(self):
        if self.ping:
            self.__status = ESTABLISHED
            return self.__status
        else:
            self.__status = NOT_FOUND
            return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    
    @property
    def time(self):
        return self.__time
    
    @time.setter
    def time(self, value):
        self.__time = value
