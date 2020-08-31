from interface.module1 import func1
from common.base import readyml
import pytest

data = readyml(r"testcase\test_data.yml")
print(data)


def test_func1_1():
    result = func1(3)
    print("测试用例1结果----%s" %result)
    assert result==4

@pytest.mark.parametrize("param",
                         [234,345])
def test_func1_2(param):
    print("-----测试用例开始-----")
    result = func1(param)
    print("测试用例结果：%s" %result)
    assert result==param+1


@pytest.mark.parametrize("data",data["input_data"])
def test_func1_3(data):
    print("-----测试用例开始-----")
    result = func1(data)
    print("测试用例结果：%s" %result)
    assert result==data+1
    print("-----测试用例结束-----")

def test_func1_4(func_fix):
    print("-----测试用例开始-----")
    result = func1(3)
    print("测试用例结果----%s" %result)
    assert result==4
    print("-----测试用例结束-----")


@pytest.mark.parametrize("fix_para",[300],indirect=True)
def test_func1_5(fix_para):
    print("-----测试用例开始-----")
    print("前置操作返回的结果：%s" %fix_para)  #先加5
    result = func1(fix_para)  #再加1
    print("测试用例结果----%s" %result)
    assert result==306
    print("-----测试用例结束-----")

@pytest.mark.parametrize("fix_para",[200],indirect=True)
def test_func1_6(fix_sec):
    print("-----测试用例开始-----")
    print("前置操作返回的结果：%s" %fix_sec)
    result = func1(fix_sec)
    print("测试用例结果----%s" %result)
    assert result==209
    print("-----测试用例结束-----")


def test_func1_7(fix_finish):
    print("-----测试用例开始-----")
    result = func1(30)
    print("测试用例结果----%s" %result)
    assert result==31
    print("-----测试用例结束-----")

@pytest.mark.parametrize("fix_all",[20],indirect=True)
def test_func1_8(fix_all):
    print("-----测试用例开始-----")
    print("前置操作返回的结果：%s" % fix_all)
    result = func1(fix_all)
    print("测试用例结果----%s" %result)
    assert result==23
    print("-----测试用例结束-----")