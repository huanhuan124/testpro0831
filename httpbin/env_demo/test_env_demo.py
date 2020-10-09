from unittest import TestCase
from httpbin.env_demo.env_demo import Env_demo
import requests
__author__ = 'zenghuan'


class TestEnv_demo(TestCase):

    def setUp(self):
        self.data = {
            "method": "get",
            "url": "http://testing:9999/demo_new.txt"

            }
        self.demo = Env_demo()

    def test_env_request(self):
        self.demo.env_request(self.data)

    def test_get_yaml(self):
        self.demo.json_to_yaml()

    def test_getaccesstoken(self):
        r = None

        # 使用锁的时候，并行执行一直卡住？？？？
        # while FileLock("session.lock"):
        # 企业微信每一个功能都有一个单独的secret，要想使用企业微信api，必须先获得access_token
        contacts_secret = 'Pt8SBjBFzFLR-_iq9BxRtk47jw7ayhlmgk567ecCKZ0'
        companyID = 'wwed0f3dc9f8233774'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + companyID + '&corpsecret=' + contacts_secret

        r = requests.get(url)
        print("test_gettoken")
        print(r.json())
        # return r.json()['access_token']