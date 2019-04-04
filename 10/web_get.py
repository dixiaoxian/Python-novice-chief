#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup as bs
import time
import random

re = request.urlopen('http://www.cninct.com/dataservices/get_suite_token')



# 配备URL
url = ['http://www.cninct.com/dataservices/get_suite_token', 'http://www.cninct.com/dataservices/get_access_token']

count = 0  # 初始化计数器
page = []

# 组装GET方法的请求

while 1:
    count += 1  # 计数器加1
    fo = open("D:/java/hello.txt", "a")
    str_5 = "现在是第%s " % count
    str__5 = "执行，时间：%s \n" % time.ctime()
    str5 = str_5 + str__5
    print(str5)
    fo.writelines(str5)
    fo.close()
    # 打印当前循环次数
    for i in range(0, url.__len__()):
        try:
            fo = open("D:/java/hello.txt", "a")
            str1 = "对应链接:%s \n" % url[i]
            fo.writelines(str1)
            resp = request.urlopen(url[i], timeout=1)
            html_data = resp.read().decode('utf-8')
            soup = bs(html_data, 'html.parser')
            str2 = "返回信息：%s \n" % soup
            print(str2)
            fo.writelines(str2)
            fo.close()
        except Exception as e:
            str3 = "出现异常:%s \n" % time.ctime()
            fo = open("D:/java/hello_err.txt", "a")
            fo.writelines(str3)
            print(str3)
            fo.close()
    fo = open("D:/java/hello.txt", "a")
    sleep_time = random.randint(10, 12)
    str4 = '等待时间：%s s \n' % sleep_time
    fo.writelines(str4)
    fo.close()
    print(str4)
    time.sleep(sleep_time)
