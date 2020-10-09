from httpbin.decrypt_demo.base_api import Base_api
import base64
import json
__author__ = 'zenghuan'

class Decrypt_demo(Base_api):

    #解密
    def decrypt_request(self,data):
        res = self.send(data)
        res_decode = base64.b64decode(res.content)
        return  json.loads(res_decode.decode('utf-8'))
