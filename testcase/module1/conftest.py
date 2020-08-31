import pytest
import os

@pytest.fixture(scope="session")
def func_fix():
    print("session范围测试用例前置操作")

@pytest.fixture(scope="function")
def fix_para(request):
    print("第一个前置操作，先加5")
    return request.param+5

@pytest.fixture(scope="function")
def fix_sec(fix_para):
    print("第二个前置操作，加上3")
    return fix_para+3

@pytest.fixture(scope="function")
def fix_finish():
    yield
    print("执行清理数据等后置操作")

@pytest.fixture(scope="function")
def fix_all(request):
    print("前置操作：给输入参数值先加2")
    yield request.param+2
    print("后置操作：执行清理数据等")


def pytest_addoption(parser):

    parser.addoption(
        "--cmdhost",         #参数名称
        action = "store",  #在命令行中遇到此参数时采取的操作
        default = "http://10.10.10.167:8000",
        help = "Run case environment"
    )

@pytest.fixture(scope="session",autouse=True)  #自动启用fixture
def value(request):
    #获取命令行参数，设置为环境变量
    os.environ["host"] = request.config.getoption("--cmdhost")    #这里貌似只能读取字符串
    print("当前默认测试环境 %s" %os.environ["host"])