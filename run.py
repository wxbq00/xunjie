#coding=utf-8
import unittest
import HTMLTestRunner
import os ,time,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
case_path=os.path.join(os.getcwd(),'case')
report_path=os.path.join(os.getcwd(),'report')
from tomorrow import threads
from BeautifulReport import BeautifulReport


#定义发送邮件
def sentmail(file_new):
#发信邮箱
    mail_from='lucas.ni@mobilenowgroup.com'
#收信邮箱
    mail_to='lucas.ni@mobilenowgroup.com'
#定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
#定义标题
    msg['Subject']=u"私有云测试报告"
#定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
#连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('imap.exmail.qq.com')
#用户名密码
    smtp.login('lucas.ni@mobilenowgroup.com','xxx')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    #log.info( 'email has send out !')
#查找测试报告，调用发邮件功能



def add_case():

    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern='start_*.py',
                                                   top_level_dir=None)

    return discover




@threads(3)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='测试报告', log_path='report')#失败重跑


# @threads(3)
# def run_case(all_case, report_path=report_path, nth=0):
#     '''执行所有的用例, 并把结果写入测试报告'''
#     report_abspath = os.path.join(report_path, "result%s.html"%nth)
#     fp = open(report_abspath, "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                            title=u'自动化测试报告,测试结果如下：',
#                                            description=u'用例执行情况：')
#
#     # 调用add_case函数返回值
#     runner.run(all_case)
#     fp.close()

if __name__ == "__main__":
    cases = add_case()

    # 之前是批量执行，这里改成for循环执行
    # for i, j in zip(cases, range(len(list(cases)))):
    #     run_case(i, nth=j)  # 执行用例，生成报告
    for i in cases:
        run(i)
