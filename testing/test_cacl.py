__author__ = 'zenghuan'
import pytest
import allure
from python import cacl

@allure.feature("测试计算器")
class  TestCacl:

    def setup(self):
        self.ca = cacl.Cacl()


    @pytest.mark.parametrize(["a","b"],[(1,2),(3,4)])
    @allure.story("测试加法")
    def test_add(self, a, b):
        result_add = self.ca.add(a,b)
        print("a+b的结果是：",result_add)


    @pytest.mark.parametrize(["a","b"],[(1,0),(2,3),(6,2)])
    @allure.story("测试除法")
    def test_div(self,a,b):
        if b == 0:
            print("报错，除数不能为0")
            raise Exception
        else:
            result_div = self.ca.div(a,b)
            print("a/b的结果是：",result_div)
        # return result_div

    def teardown(self):
        pass

