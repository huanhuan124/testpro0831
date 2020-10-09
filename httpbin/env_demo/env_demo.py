from httpbin.env_demo.base_api import Base_api

__author__ = 'zenghuan'


class Env_demo(Base_api):


    def env_request(self,data):
        res = self.send(data)
        print(res.text)

