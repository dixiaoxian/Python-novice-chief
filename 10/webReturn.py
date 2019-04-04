import urllib.request
from urllib import request
from bs4 import BeautifulSoup as bs
import time
import random

# 配备URL
url = ['http://www.cninct.com/gmoon/get_suite_token', 'http://www.cninct.com/gmoon/get_access_token',\
       'http://www.cninct.com/dataservices/get_suite_token','http://www.cninct.com/dataservices/get_access_token',\
       'http://www.cninct.com/dataservices/get_access_token_4a']


# 组装GET方法的请求

fo = open("C:/Users/Administrator/Desktop/web_access.log", "a")
str5 = "执行时间：%s \n" % time.ctime()
fo.write(str5)
fo.close()
# 打印当前循环次数
for i in range(0, url.__len__()):
    try:
        fo = open("C:/Users/Administrator/Desktop/web_access.log", "a")
        str1 = "对应链接:%s \n" % url[i]
        fo.write(str1)
        resp = request.urlopen(url[i], timeout=10)
        # file = urllib.request.urlopen(url[i], timeout=10) #设置超时时间
        html_data = resp.read().decode('utf-8')
        soup = bs(html_data, 'html.parser')
        str2 = "返回信息：%s \n" % soup
        fo.writelines(str2)
        fo.close()
    except Exception as e:
        str3 = "出现异常:%s \n" % time.ctime()
        fo = open("C:/Users/Administrator/Desktop/web_err.log", "a")
        fo.write(str3)
        fo.close()
fo = open("C:/Users/Administrator/Desktop/web_access.log", "a")
str4 = '等待时间：1小时 s \n'
fo.write(str4)
fo.close()
