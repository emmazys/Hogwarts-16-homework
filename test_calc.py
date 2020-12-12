import pytest
from pythoncode.calculator import Calculator
class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")
    # 加法
    @pytest.mark.parametrize("a,b,expect",[
        (0,0,0),(3,5,8),(-1,-2,-3),(100,300,400)
    ],ids=["zero","int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)

    # 减法
    @pytest.mark.parametrize("a,b,expect", [
        (0,0,0),(2,1,1), (-1,-2,1), (500,300,200)
    ], ids=["zero","int", "minus", "bigint"])
    def test_sub(self,a,b,expect):
        assert expect == self.calc.sub(a,b)

    # 乘法
    @pytest.mark.parametrize("a,b,expect", [
        (0,0,0),(2,1,2), (-1,-2,2), (500,300,150000)
    ], ids=["zero","int", "minus", "bigint"])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)

    # 除法
    @pytest.mark.parametrize("a,b,expect", [
        (0,1,0),(2,1,2), (-1,-2,0.5), (1500,300,5)
    ], ids=["zero","int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a,b)