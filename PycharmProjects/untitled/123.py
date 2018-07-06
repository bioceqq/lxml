import pymysql.cursors
# import numpy as np
# import pandas as pd

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='vipqq',
    db='qq',
    charset='UTF8'
)

# 获取游标
cursor = connect.cursor()
#打印所有数据
# sql = "select * from urls"

sql_insert ="""insert into urls(id,url,content) values(5,'www.sina.com','xinlang')"""
try:
    cursor.execute(sql_insert)
    connect.commit()

    print("charu")
except Exception as e:
    connect.rollback()
finally:
    connect.close()
# sql1 = "insert into urls id Values (2)"
# cursor.execute(sql)
# rx=cursor.fetchall()
# print(rx)
# # a=list(cursor.fetchall())
# # b=pd.DataFrame(a,index=["one","two","three","four"],columns=["序号","姓名","联系方式","薪资","其他","备注"])
# # c=b.iloc[:,0:4]
# # print(c.sort())
# cursor.close()
# connect.close()
#
