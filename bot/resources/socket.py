from .response import Response
from .exceptions import ServerNotFound, SomethingWentWrong
from .connection import ConnectionEstablished
import requests


class Botquery():
    def __init__(self, ip, port = None):
        self.ip = ip
        self.port = port
        self.connection = ConnectionEstablished()
        self.data = self.connection.data
        self.run()

    def run(self):
        while self.connection.ping is not True:
            try:
                response = Response(self.ip, self.port)
                request = requests.get(response.msg)

                data = request.json()
                self.data = data
                ping = data['online']
                self.connection.ping = ping
                print(self.connection)

                if self.connection.ping is not True:
                    request = requests.get(response.api + response.url)
                    data = request.json()
                    self.data = data

                    ping = data['online']
                    self.connection.ping = ping
                    print(self.connection)
                    
                
                self.connection.time =  self.connection.time + 1
                if self.connection.time == 10:
                    raise ServerNotFound

            except SomethingWentWrong:
                pass
    