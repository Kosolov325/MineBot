from resources.response import Response
from resources.exceptions import ServerNotFound, SomethingWentWrong
from resources.connection import ConnectionEstablished
import requests


class Botquery():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.run(self)

    def run(self):
        connection = ConnectionEstablished(None)

        while connection.ping is not True:
            try:
                response = Response(self.ip, self.port)
                request = requests.get(response.msg)

                data = request.json()
                debug = data['debug']
                ping = debug['ping']
                connection.ping = ping
                if connection.ping is not True:
                    request = requests.get(response.api + response.url)
                    data = request.json()
                    debug = data['debug']
                    ping = debug['ping']
                    connection.ping = ping

                connection.time =  connection.time + 1
                if connection.time == 10:
                    raise ServerNotFound

                print(connection)
            except SomethingWentWrong:
                pass