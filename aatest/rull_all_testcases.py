import unittest
import time
from aatest import HTMLTestReport
import os





current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())) #生成报告的时间
# case_path = os.getcwd()    # 用例路径    os.getcwd()代表返回当前工作目录
case_path = r"./"  #设置指定路径
report_path = os.path.join(case_path, 'report_'+current_time+".html") # 报告存放路径
def all_case():
    #批量调用用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)    #case_path可以用字符串来表示　　test*.py表示test前缀的py文件　　top_level_dir= None 测试模块的顶层目录，如果没有顶层目录，默认为None
    print(discover)  #F失败的　Ｅ通过的　多少个表示多少个用例
    return discover
if __name__ == "__main__":
    #打开路径，用二进制写入
    fp = open(report_path, "wb")
    # 构建测试套件
    #用网页的形式显示测试报告
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title="自动化测试报告", description='关于H6项目接口测试报告', tester='韩宝俊')
    runner.run(all_case())
    fp.close()

