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

    smtp = smtplib.SMTP ()
    smtp.connect ('smtp.163.com')
    sender = '17372253210@163.com'
    receiver = '17372253210@163.com'
    username = '17372253210@163.com'
    password = 'qweqwe123'
    smtp.login (username, password)

    subject1 = 'python send email test'
    print(subject1)
    msg = MIMEText (filename, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    msg['From'] = '陈功<17372253210@163.com>'
    msg['To'] = '17372253210@163.com'
    smtp.sendmail (sender, receiver, msg.as_string ())
    smtp.quit ()

    print ('email has send out!')


# ===========================查找测试报告目录，找到最新的测试报告文件 ===========================
def new_report(testreport):
    lists = os.listdir (testreport)
    lists.sort (key=lambda fn: os.path.getmtime (testreport + "\\" + fn))
    file_new = os.path.join (testreport, lists[-1])
    print (file_new)
    return file_new

# 发送附件测试
#     sendfile = open('C:\\Users\\Administrator\\PycharmProjects\\cgtest_scripts\\raport\\result.html','rb').read()
#     att = MIMEText(sendfile,'base64','utf8')
#     att["Content-Type"] = 'application/octet-stream'
#     att["Content-Disposition"] = 'attachment; filename="result.html"'
#     msgRoot = MIMEMultipart('related')
#     msgRoot['Subject'] = subject1
#     msgRoot.attach(att)




if __name__ == "__main__":
    test_dir = r'C:\Users\Administrator\PycharmProjects\SeleniumTest\runtest'
    test_report = r'C:\Users\Administrator\PycharmProjects\SeleniumTest\report'
    discover = unittest.defaultTestLoader.discover (test_dir, pattern='test*.py')

    now = time.strftime ("%Y-%m-%d_%H_%M_%S")
    filename1 = test_report + '\\' + now + 'result1.html'
    fp = open (filename1, 'wb')

    # runner = HTMLTestReport.HTMLTestRunner (stream=fp, title=u"自动化测试报告", description='自动化测试演示报告', tester='fyr')
    runner = HTMLTestRunner (stream=fp, title='集成测试报告', description='测试用例执行情况')
    runner.run (discover)
    fp.close ()

    new_report = new_report (test_report)
    send_mail (new_report)  # 发送测试包