__author__ = 'zenghuan'

import pytest
@pytest.fixture()
def login():
    print("这是登录模块，放在conftest文件中")


def pytest_collection_modifyitems(session, config, items):
    # print(items)
    # print(type(items))
    items.reverse()
    # print(items)
    # for item in items:
    #     if "case1" in item.nodeid:
    #         item.add_marker(pytest.mark.case1)
    #     elif "one" in item.nodeid:
    #         item.add_marker(pytest.mark.one)
