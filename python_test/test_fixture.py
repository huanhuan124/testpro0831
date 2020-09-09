__author__ = 'zenghuan'

import sys
import pytest
sys.path.append("../")
# @pytest.fixture()
# def login():
#     print("这是登录模块")

def test_case1(login):
    print("这是第1个用例，需要先登录")

def test_case2():
    print("这是第2个用例，不需要登录")

def test_case3(login):
    print("这是第3个用例，需要先登录")

# if __name__ == '__main__':
#     pytest.main()