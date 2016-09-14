#!/bin/env python
#coding=utf-8*#
from bs4 import BeautifulSoup
import urllib2
import cookielib
import json
import sys
import ssl
from pprint import pprint
import threading
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

reload(sys)
sys.setdefaultencoding('utf-8')
url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-09-28&from_station=DMQ&to_station=MDQ'
context = ssl._create_unverified_context()
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
count = 1

mail_info = {
    "from": "2221348095@qq.com",
    "to": "2221348095@qq.com",
    "hostname": "smtp.qq.com",
    "username": "2221348095@qq.com",
    "password": "jxpgpdzzjxeieach",
    "mail_subject": "test",
    "mail_text": "hello, this is a test email, sended by py",
    "mail_encoding": "utf-8",
    "port": 465
}

def getTicket():
    global count
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url, context=context)
    result = json.loads(response.read())
    print count
    if result['data'][u'datas'][2][u'station_train_code'].encode('utf-8') == 'K836' and result['data'][u'datas'][2][u'yw_num'].encode('utf-8') == '无':
        print 'There is no ticket to maoming yet.'
    elif result['data'][u'datas'][2][u'station_train_code'].encode('utf-8') == 'K836' and result['data'][u'datas'][2][u'yw_num'].encode('utf-8') != '无':
        print 'There is tickets to maoming.'

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText('发现有从东莞到茂名的火车票，快快去订！！！', 'plain', 'utf-8')
        message['From'] = Header("来自Kevin同学的刷票小能手", 'utf-8')
        message['To'] = Header("测试", 'utf-8')

        subject = '有到茂名的火车票！！！'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = SMTP_SSL(mail_info["hostname"], mail_info["port"])
            smtpObj.ehlo(mail_info["hostname"])
            smtpObj.set_debuglevel(1)
            smtpObj.login(mail_info["username"], mail_info["password"])
            smtpObj.sendmail(mail_info["from"], mail_info["to"], message.as_string())
            print "邮件发送成功"
        except SMTP_SSL.SMTPException:
            print "Error: 无法发送邮件"
    count += 1
    global t
    t = threading.Timer(6,getTicket)
    t.start()

t = threading.Timer(6,getTicket)
t.start()




