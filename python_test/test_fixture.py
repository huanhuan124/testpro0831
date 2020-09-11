__author__ = 'zenghuan'

import sys
import pytest

sys.path.append("../")
# @pytest.fixture()
# def login():
# print("这是登录模块")
class Test_fixture_login:


    def test_case1(slef,login):
        print("这是第1个用例，需要先登录")


    def test_case2(self):
        print("这是第2个用例，不需要登录")


    def test_case3(self,login):
        print("这是第3个用例，需要先登录")


if __name__ == '__main__':
    pytest.main(["-sv","test_fixture.py"])