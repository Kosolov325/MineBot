class Response():
    def __init__(self, url, port):
        if url is None:
            url = ""
        if port is None:
            port = '25565'

        self.__url = url
        self.__port = ':' + port
        self.__api = "https://api.mcsrvstat.us/2/"
        self.__msg = self.__api + self.__url + self.__port
    
    @property
    def url(self):  
        return self.__url
    
    @url.setter
    def url(self,value):
        self.__url = value
    
    @property
    def port(self):  
        return self.__port
    
    @port.setter
    def port(self,value):
        self.__port = value
    
    @property
    def api(self):  
        return self.__api

    @property
    def msg(self):
        return self.__msg