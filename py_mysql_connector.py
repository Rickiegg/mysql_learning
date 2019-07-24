# -*- coding: UTF-8 -*-
import mysql.connector
import pymysql
import traceback
# 打开数据库连接
# db = mysql.connector.connect() #会因为mysql版本密码强弱报错，用pymysql来解决
db_host = "localhost"
db_username = "root"
db_password = "Rimysql2019"
db_name = "test_db"

db = pymysql.connect(
host=db_host,
user=db_username,
passwd=db_password,
database=db_name,
)
# 获取操作游标 
cursor = db.cursor()
# 执行 SQL 语句

# 插入新球员
sql = "INSERT INTO player (team_id, player_name, height) VALUES (%s, %s, %s)"
val = (1003, " 约翰 - 科林斯 ", 2.08)

cursor.execute(sql, val)
db.commit()
sql = "select * from player"
cursor.execute(sql)
print(cursor.rowcount, " 记录插入成功。")

# 关闭游标 & 数据库连接
cursor.close()
db.close()

# try...except捕获异常信息
try:
  sql = "INSERT INTO player (team_id, player_name, height) VALUES (%s, %s, %s)"
  val = (1003, " 约翰 - 科林斯 ", 2.08)
  cursor.execute(sql, val)
  db.commit()
  print(cursor.rowcount, " 记录插入成功。")
except Exception as e:
  # 打印异常信息
  traceback.print_exc()
  # 回滚  
  db.rollback()
finally:
  # 关闭数据库连接
  cursor.close()
  db.close()


