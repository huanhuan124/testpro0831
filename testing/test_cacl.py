from python import cacl
import pytest
import allure
from decimal import Decimal,getcontext

@allure.feature("测试计算器功能")
class TestCacl:


    def setup(self):
        self.cal = cacl.Cacl()


#浮点数运算时，需要加入Decimal函数进行精度处理
    @allure.story("测试加法正常情况")
    @pytest.mark.parametrize(["a","b","c"],[(1,2,3),(100,200,300),(0,0,0),(-2,-3,-5),(-9,6,-3),(0,-9,-9),(0,4,4)])
    def test_add(self,a,b,c):
        result = self.cal.add(a,b)
        assert result == c

    @allure.story("测试加法浮点数情况")
    @pytest.mark.parametrize(["a","b","c"],[(0.1,0.2,0.3)])
    def test_add_float(self,a,b,c):
        #getcontext().prec  固定小数点后面的位数
        #想要固定控制小数点后面的位数则需要使用decimal.quantize(Decimal('0.00000000'))，注意不能超过getcontext().prec的位数
        getcontext().prec = 9
        result = self.cal.add(a,b)
        result = Decimal(result).quantize(Decimal("0.0"))
        assert result == Decimal(c).quantize(Decimal("0.0"))


    @allure.story("测试除法的正常情况")
    @pytest.mark.parametrize(["a", "b", "c"],
                             [(1, 2, 0.5), (100, 200, 0.5), (0, 1, 0),(-2, -1, 2.0), (-9, 6, -1.5)])
    def test_div_normal(self,a,b,c):
        result = self.cal.div(a,b)
        assert result == c




    @allure.story("测试除法的异常情况，除数为0，抛出异常")
    @pytest.mark.xfail
    @pytest.mark.parametrize(["a","b"],[(1,0)])
    def test_div_except(self,a,b):
        raise ZeroDivisionError

# pytest.main()
if __name__ == '__main__':
    # TestCacl()
    pytest.main(["-s", "test_cacl.py"])