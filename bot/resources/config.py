import os
import json

class Config:
    def __init__(self, token, api, prefix):
        self.__token = token
        self.__api = api
        self.__prefix = prefix
    
    @property
    def token(self):
        return self.__token

    @property
    def api(self):
        return self.__api

    @api.setter
    def api(self,value):
        self.__api = value
    
    @property
    def prefix(self):
        return self.__prefix
    
    @prefix.setter
    def prefix(self,value):
        self.__prefix = value

workspace = os.getcwd()
config_dir = '/config/config.json'
config_path = workspace + config_dir
config_file = open(config_path, 'r')
data = json.load(config_file)

default_token = data['token']
default_api = data['api']
default_prefix = data['prefix']

botconfig = Config(default_token, default_api, default_prefix)