# -*- coding: utf-8 -*-

import time
import unittest
import HTMLTestRunner

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from email.header import Header
import smtplib
import os

# 加载测试文件
import case.j_expense_case.test_agree_expense_case as cec
import case.e_fee_type_case.test_ea_new_auto_fee_type_case as nftc

# 构建测试集
# suite = unittest.TestSuite()
# suite.addTest(nftc.TestNewFee('test_new_fee'))
# suite.addTest(cec.TestNewExpense("test_new_expense"))


# --------定义发送邮件-------
def send_mail(file_new):
    # f = open(file_new, 'rb')
    # mail_body = f.read()
    # f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户、密码
    user = '17372253210@163.com'
    password = 'qweqwe123'
    # 发送邮箱
    sender = '17372253210@163.com'
    # 接受邮箱
    receiver = '17372253210@163.com'
    # 发送邮箱主题
    subject = u'自动化测试报告'

    msg = MIMEMultipart()
    # msg = MIMEText( 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '17372253210@163.com'
    msg['To'] = '17372253210@163.com'
    puretext = MIMEText('纯文本内容', 'utf-8')
    msg.attach(puretext)

    # jpgpart = MIMEApplication(open('/Users/wei/PycharmProjects/dingding2.0/runtest/ +  ', 'rb').read())
    jpgpart = MIMEApplication(open(file_new, 'rb').read())

    jpgpart.add_header('Content-Disposition', 'attachment', filename='latest_report.html')
    msg.attach(jpgpart)

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

    print ('email has send out!')

# --------查找测试报告目录，找到最新生成的测试报告文件-----


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "/" + fn))
    file_name = os.path.join(testreport, lists[-1])
    print (file_name)
    return file_name

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    test_dir = 'case'
    test_report = 'C:\\Users\\Administrator\\Desktop\\selenium\\selenium-python-scripts-master\\runtest'
    # discover（）方法
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # 按照一定格式获取当前时间
    # now = time.strftime("%Y-%m-%d %H:%M:%S")
    # result = 'result.html'

    filename = 'C:\\Users\\Administrator\\Desktop\\selenium\\selenium-python-scripts-master\\runtest' + time.strftime("%Y-%m-%d %H:%M:%S") + 'result.html'

    filename1 = 'C:\\Users\\Administrator\\Desktop\\selenium\\selenium-python-scripts-master\\runtest\\test.txt'
    fp = open(filename1, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'2.0测试报告', description=u'用例执行情况')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)

