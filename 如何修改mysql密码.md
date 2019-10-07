# 如何修改mysql root密码

先停掉所有mysql服务
```

$ sudo su

$ cd /usr/local/mysql/bin

$ ./mysqld_safe --skip-grant-tables --skip-networking &
```
这时，新建一个终端窗口，不过不要关闭当前的。

输入：
```
$ cd /usr/local/mysql/bin/

$ mysql -u root
```
成功了！出现了让人舒心的 mysql> 提示符。

正确修改root密码的步骤为： 

步骤1.如果当前root用户authentication_string字段下有内容，先将其设置为空，没有就跳到步骤 2。
```
    use mysql; 
    update user set authentication_string='' where user='root'
```
步骤2.使用ALTER修改root用户密码,方法为：
```
    use mysql；
    ALTER user 'root'@'localhost' IDENTIFIED BY '新密码';
    FLUSH PRIVILEGES;
```
设置root密码 注意：在MySQL 5.7.9以后废弃了password字段和password()函数
```
alias mysql=/usr/local/mysql/bin/mysql
```
`mysql -u root -p`输入密码即可连接