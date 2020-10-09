import requests

__author__ = 'zenghuan'

class Base_api:

    #封装request
    def send(self,data):
       return requests.request(data['method'],data['url'])