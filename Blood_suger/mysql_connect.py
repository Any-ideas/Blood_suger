# -*- coding: utf-8 -*-
"""
-------------------------------
@Project :Python_Flask  
@File    :mysql_connect.py
@IDE     :PyCharm
@Author  :YZ
@Date    :2024/1/7 9:24
-------------------------------
"""
db_config = {
    "host": "47.101.212.166",
    "port": 3306,
    "user": "root",
    "password": "19991025yuzhen@",
    "db": "blood_suger",
    "charset": "utf8",
}

import pymysql

def execute_sql(sql, args=None):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute(sql, args)
        connection.commit()
        data = cursor.fetchall()
        return data
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    sql = "SELECT * FROM daydata WHERE userId = 1"
    data = execute_sql(sql)
    print(data)