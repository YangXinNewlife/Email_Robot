# -*- coding:utf-8 -*-  
from email.mime.text import MIMEText  
from email.header import Header
import smtplib

class email_server(object):
    def __init__(self):
        pass

    @staticmethod
    def send_email():
        msg = MIMEText("Dear User,I am Ryan's assistant. Thr Robot Mr.Xin. Gears Server Error，Import Failed",'plain','utf-8')
        msg['From'] = Header("Ryan",'utf-8')
        msg['To'] = Header('MYSelf','utf-8')
        subject = 'Gears Server Message'
        msg['Subject'] = Header(subject,'utf-8')
        #sender
        from_addr = 'xxx@qq.com'
        #password
        password = 'xxx'
        #smtp server
        smtp_server = 'smtp.qq.com'
        #receiver
        to_addr = 'xxx@163.com'
        #ssl model
        server = smtplib.SMTP_SSL(smtp_server,465)
        # debug model
        server.set_debuglevel(1)

        #login ssl server
        server.login(from_addr,password)
        # send message
        server.sendmail(from_addr,[to_addr],msg.as_string())
        # login out
        server.quit()

email_server.send_email()