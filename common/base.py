import os
import yaml

def readyml(ymlpath):
    """
    读取yaml文件内容
    :param ymlpath: yml文件路径，传入以项目根目录为基准开始的路径）
    """
    # realpath获取带文件名的绝对路径，dirname获取上一级路径
    basePath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    filepath = os.path.join(basePath, ymlpath)
    if not os.path.isfile(filepath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % filepath)
    # open方法打开直接读出来
    f = open(filepath, "r", encoding="utf-8")
    cfg = f.read()
    #print(cfg)
    # load方法转成字典
    d = yaml.safe_load(cfg)
    return d


if __name__ == '__main__':
    data = readyml(r"testcase\test_data.yml")
    print(data)