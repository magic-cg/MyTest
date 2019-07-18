# -*- coding: utf-8 -*-

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import unittest
import time
import os


# ******************定义发送邮件******************
def send_mail(file_new):
    f = open (file_new, 'rb')
    filename = f.read ()
    f.close ()

    msg = MIMEText(filename, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')


    smtp = smtplib.SMTP ()
    smtp.connect ('smtp.163.com')
    sender = '17372253210@163.com'
    receiver = '871362095@qq.com'
    username = '17372253210@163.com'
    password = 'qweqwe123'
    smtp.login (username, password)



    msg['From'] = '陈功<17372253210@163.com>'
    msg['To'] = '871362095@qq.com'
    smtp.sendmail (sender, receiver, msg.as_string ())
    smtp.quit ()

    print ('***程序运行完成，邮件发送成功！')


# ===========================查找测试报告目录，找到最新的测试报告文件 ===========================
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print (file_new)
    return file_new



if __name__ == '__main__':
    test_dir = r'C:\Users\Administrator\PycharmProjects\SeleniumTest\case'
    test_report = r'C:\Users\Administrator\PycharmProjects\SeleniumTest\report'
    discover = unittest.defaultTestLoader.discover (test_dir, pattern='test*.py')

    now = time.strftime ("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='集成测试报告', description='测试用例执行情况')
    runner.run (discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)  # 发送测试包