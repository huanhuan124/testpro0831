__author__ = 'zenghuan'


import pytest
class Test_demo():
    def test_case1(self):
        print("开始执行testcase1 ***")
        # assert 'h' in "this"
        pytest.assume( 'h' in "this")
        pytest.assume(1==2)
        pytest.assume( 'a' in "abc")
        pytest.assume( 'a' in "1111")

    def test_case2(self):
        print("开始执行testcase2 ***")
        assert 'h' in "AA"


    def test_case3(self):
        print("开始执行testcase3 ***")

class Test_demo1():
    def test_one(self):
        print("开始执行testone ***")
        assert 'h' in "this"

    def test_two(self):
        print("开始执行testtwo ***")
        assert 'h' in "32"


    def test_three(self):
        print("开始执行testthree ***")


if __name__ == '__main__':
    pytest.main()
    # pytest.main("-v -x Test_demo")
    # pytest.main(['-v','-s','Test_demo'])