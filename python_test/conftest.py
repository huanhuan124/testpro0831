__author__ = 'zenghuan'

import pytest
@pytest.fixture()
def login():
    print("这是登录模块，放在conftest文件中")