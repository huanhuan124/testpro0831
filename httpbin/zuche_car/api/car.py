from httpbin.zuche_car.api.base_api import Base_api

__author__ = 'zenghuan'
import requests


class Car(Base_api):



    def login(self):
        data = {
            "method":"post",
            "url":"http://caradmintest.zuche.com/system/login.do_",
            "data":{
                "loginId": "UA244Y8SbzJRKNVluixyKA==",
                "password": "qLpmhT5PIxYdFCh/kZ+dcw=="
            }
        }

        lg_res = self.send(data)
        print(lg_res.text)
        return  lg_res.cookies

    def getCarInfo(self,data):

        res = self.send(data)
        return res