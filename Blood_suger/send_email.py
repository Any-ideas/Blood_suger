# _*_ Coding : UTF-8 _*_
# @Time :  15:25
# @Author : YYZ
# @File : 阿里云监控
# @Project : Python_Project_爬虫
'''
健康阿里云需要预先安装两个组件
pip install aliyun-python-sdk-core   -i https://mirrors.aliyun.com/pypi/simple/
pip  install   aliyun-python-sdk-bssopenapi  -i https://mirrors.aliyun.com/pypi/simple/
pip install PyEmail
'''

import pymysql
import mysql_connect
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#163邮箱
host_servier = 'smtp.163.com'
#登入网易邮箱的账户
sender_mail = 'y13151552592@163.com'
#163邮箱授权码
pwd = 'LNEWVGQMZTWJWNLE'
#发件人名称
sender_163_mail = '检测平台'
#阈值
Decimal = 1000

#发送邮件
def  send_mail(email):
    # 收件人邮箱
    receiver = f'{email}'
    # 邮件的正文内容
    mail_content = '您有尚未完成的血糖检测的任务'
    # 邮件标题
    mail_title = '警告！！！'

    #ssl登录
    smtp = smtplib.SMTP_SSL(host_servier)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    #shlo 申明自己的身份
    smtp.ehlo(host_servier)
    smtp.login(sender_mail,pwd)
    #邮件内容
    msg = MIMEText(mail_content,"plain",'utf-8')
    #邮件标题
    msg["Subject"] = Header(mail_title,'utf-8')
    #邮件发件人名称
    msg["From"] = sender_163_mail
    #收件人
    msg["To"] = receiver
    smtp.sendmail(sender_mail,receiver,msg.as_string())
    smtp.quit()
    print(str(email)+"：发送完成")
'''
head：类似实体邮件的封面信息
—Subject：主题
—From：来自谁，发送者对自己的昵称，可以随便
—To：发送者对接收者的昵称，可以随便
context：类似实体邮件的内部的内容
'''

def select_user():
    sql = "SELECT  post.content, post.userId, post.title, user.email FROM post JOIN user ON post.userId = user.id;"
    data = mysql_connect.execute_sql(sql)
    # print(data)
    # email = [item[3] for item in data]
    email = set(item[3] for item in data if item[3] is not None)
    # title = set(item[2] for item in data if item[2] is not None)
    # content = set(item[0] for item in data if item[0] is not None)
    #print(email)
    return email

if __name__ == '__main__':
    email_list = select_user()
    for email in email_list:
        send_mail(email)