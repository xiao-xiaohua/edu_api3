import unittest
import time
from HTMLTestReportCN import HTMLTestRunner    #第三方的库模块,测试报告模板
from libs.tools import (send_email,GetNewReport )
from config.Secret import (email_account,email_to_account,email_port,email_pwd)



# verbosity
# 0:代表只显示结果
# 1:默认值 .. .f之类
# 2.显示详细的用例执行信息


def run_test():
    # 找到需要执行的脚本的目录
    dirpath = './Scripts'
    # 指定运行脚本的目录以及具体的问题 *_dc.py 代表匹配后面的内容
    discover = unittest.defaultTestLoader. \
        discover(dirpath, pattern='*_dc.py')
    # 对当前时间戳进行格式化
    currenttime = time.strftime('%y%m%d%H%M%S')
    # 生成测试报告名称
    filedir = './reports/' + 'report' + currenttime + '.html'
    #创建测试报告，不需关闭文件这个动作
    with open(filedir,'wb') as fp:
    # 报告格式
        runner = HTMLTestRunner(stream=fp, title='counter程序测试报告',
                                             description='测试报告描述',
                                             tester='张晓华',verbosity=2)
    # 执行脚本
        runner.run(discover)
    #生成的测试报告按时间倒序排列
    f = GetNewReport()
    #发送邮件
    send_email(email_account,email_pwd,email_port,email_to_account,'测试报告已完成，请查收','自动化测试报告',f)
    print('发送成功')

if __name__ == '__main__':
    run_test()



