import pymysql
def db(DBname):
    pymysql.connect("192.168.1.152", "root", "123456", DBname) # 若是本地数据库，将192.168.1.152改成localhost(主机地址、用户、密码、数据库名)