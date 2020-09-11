__author__ = 'zenghuan'
import pytest

# fixtures documentation order example
order = []


@pytest.fixture(scope="session")
def s1():
    print("s1,作用于是session")
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    print("m1,作用于是module")
    order.append("m1")


@pytest.fixture
def f1(f3):
    print("f1,作用于是fuction")
    order.append("f1")

# @pytest.fixture
# def f4(f3):
#     print("f4,作用于是fuction")
#     order.append("f4")

@pytest.fixture
def f3():
    print("f3,作用于是fuction")
    order.append("f3")


@pytest.fixture(autouse=True)
def a1():
    print("a1,作用于是fuction,autouse自动执行，优于同级作用域")
    order.append("a1")


@pytest.fixture
def f2():
    print("f2,作用于是fuction")
    order.append("f2")


def test_order(f1, m1, f2, s1):
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]