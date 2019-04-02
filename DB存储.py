from urllib import request
from bs4 import BeautifulSoup as bs
import pymysql

# 页面链接
url = 'https://www.meishij.net/china-food/caixi/'
html = request.urlopen(url)
html_data = html.read().decode('utf-8')

# 解析页面
soup = bs(html_data, 'html.parser')
shicai = soup.find_all('div', class_='listtyle1')

# 拿到菜名和链接
for i in shicai:
    shicai_file = i.find_all('a')
    # 得到列表，不能解析
    # print(shicai_file)
    # 读取每个列表的内容
    for i in shicai_file:
        # 分析得到'title标签'为菜名,'href标签'为链接
        filename = i['title']
        filehtml = i['href']

        # 打开数据库连接
        db = pymysql.connect("192.168.1.74", "root", "123456",
                             "numData")  # 若是本地数据库，将192.168.1.152改成localhost(主机地址、用户、密码、数据库名)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # sql语句
        sql = 'INSERT INTO file (filename,filehtml) VALUES ("%s","%s")' % (filename, filehtml)
        try:
            # 使用 execute()  方法执行 SQL 语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            print("存储错误")
            db.rollback()
        # 关闭数据库连接
