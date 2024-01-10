# -*- coding: utf-8 -*-
"""
-------------------------------
@Project :Python_Flask  
@File    :insert_mysql.py
@IDE     :PyCharm
@Author  :YZ
@Date    :2024/1/6 22:42
-------------------------------
"""
import pymysql
from datetime import datetime
import select_mysql

def insert_user(userAccount,userPassword):
    connection = pymysql.connect(host="47.101.212.166", port=3306, user='root', password='19991025yuzhen@', charset='utf8',
                             db='blood_suger')
    # 连接数据库之后，基于cursor去发送指令
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(f"select userPassword from user where userAccount='{userAccount}'")
    res = cursor.fetchall()
    if res:
        print("用户已存在")
        return 1
    else:
        with connection.cursor() as cursor:
            # 执行插入操作
            sql = """
                   INSERT INTO user ( userAccount, userPassword, createTime, updateTime)
                   VALUES (%s, %s, %s, %s)
                   """
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(sql, ( userAccount, userPassword, current_time, current_time))
        # 提交事务
        connection.commit()
        return 0



if __name__ == '__main__':
    insert_user('aa','aa')
