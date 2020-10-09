from unittest import TestCase
from httpbin.decrypt_demo.decrypt_demo import Decrypt_demo
import base64
import json
__author__ = 'zenghuan'


class TestDecrypt_demo(TestCase):

    #测试解密
    def test_decrypt_request(self):
        data = {
            "method":"get",
            "url":"http://127.0.0.1:9999/demo_new.txt"
        }
        demo = Decrypt_demo()
        demo.decrypt_request(data)


