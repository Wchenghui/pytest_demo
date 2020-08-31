import pytest
from common.base import readyml
from interface.module1 import func2
import os


data = readyml(r"testcase\test_data.yml")


@pytest.mark.parametrize("input,expect",data["func2_data"])
def test_func2_1(func_fix,input,expect):
    print("-----测试用例开始-----")
    print("测试参数：x=%s，y=%s" %(input["x_data"],input["y_data"]))
    result = func2(x=input["x_data"],y=input["y_data"])
    print("测试用例结果：%s" %result)
    assert result==expect
    print("-----测试用例结束-----")