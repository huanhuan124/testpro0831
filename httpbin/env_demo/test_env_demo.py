from unittest import TestCase
from httpbin.env_demo.env_demo import Env_demo

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
        self.demo.get_yaml()