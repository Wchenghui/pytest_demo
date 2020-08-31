import pytest
import os
import allure

def test_4():
    print("测试用例4")
    print("当前测试环境：%s" %os.environ["host"])

@pytest.mark.usefixtures("func_fix")
class TestDemo:
    def test_1(self):
        print("测试用例1")

    def test_2(self):
        print("测试用例2")

def test_3(func_fix):
    print("测试用例3")

@pytest.mark.skip("跳过此用例")
def test_5(func_fix):
    print("测试用例3")