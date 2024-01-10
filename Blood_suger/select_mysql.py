# -*- coding: utf-8 -*-
"""
-------------------------------
@Project :Python_Flask  
@File    :select_mysql.py
@IDE     :PyCharm
@Author  :YZ
@Date    :2024/1/6 21:46
-------------------------------
"""

import pymysql
import json

def select_user(userAccount,userPassword):
    # 链接数据库
    connet = pymysql.connect(host="47.101.212.166", port=3306, user='root', password='19991025yuzhen@', charset='utf8',
                             db='blood_suger')
    # 连接数据库之后，基于cursor去发送指令
    cursor = connet.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(f"select * from user where userAccount='{userAccount}'")
    res = cursor.fetchall()
    print(res[0]['userPassword'])
    if res:
        res_passwd = res[0]
        if res_passwd["userPassword"] == userPassword:
            cursor.close()
            connet.close()
            return 0,res_passwd['id'],res
    # elif res_passwd["userPassword"]:
    #     return 1
    else:
        cursor.close()
        connet.close()
        return 1


if __name__ == '__main__':
    userAccount = 'admin'
    userPassword = '12345678'
    res = select_user(userAccount,userPassword)
    print(res)


