# 使用python 连接数据库

利用pymysql进行连接
```
    import pymysql
    # 打开数据库连接
    # db = mysql.connector.connect() #会因为mysql版本密码强弱报错，用pymysql来解决
    db_host = "localhost"
    db_username = "root"
    db_password = "Rimysql2019"
    db_name = "test"
    db = pymysql.connect(host=db_host,user=db_username,passwd=db_password,database=db_name,)
```
1. 使用游标cursor进行数据库操作,fetchall()为逐条操作

    ```python
    sql_text = 'SELECT * FROM bread_basket'
    cursor = db.cursor()
    cursor.execute(sql_text) # 执行操作
    data1 = cursor.fetchall()
    # 关闭游标 & 数据库连接

    cursor.close()
    db.close()
    data1
```
1. 用sqlalchemy创建连接引擎，用pandas读取数据，结构为DataFrame
```
    import sqlalchemy as sql
    engine = sql.create_engine('mysql+pymysql://root:Rimysql2019@localhost/test')  
    query = 'SELECT * FROM bread_basket'
    data = pd.read_sql(query, engine)
    data
```