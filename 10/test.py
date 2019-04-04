#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import random
import time    # 时间函数库，包含休眠函数sleep()

#博客园

#博客c
# 1-https://blog.csdn.net/qq_41116956/article/details/84105041 java&python对比 5
# 2-https://blog.csdn.net/qq_41116956/article/details/80595285  1 5
# 3-https://blog.csdn.net/qq_41116956/article/details/80581624  安装tomcat  6
# 4-https://blog.csdn.net/qq_41116956/article/details/84105734  jenkins   6
# 5-https://blog.csdn.net/qq_41116956/article/details/82661381   sudo命令    5
# 6-https://blog.csdn.net/qq_41116956/article/details/82697164 Ubuntu源     4
# 7-https://blog.csdn.net/qq_41116956/article/details/82767078 修改ip    6
# 8-https://blog.csdn.net/qq_41116956/article/details/82704365 xfs备份恢复     6
# 9-https://blog.csdn.net/qq_41116956/article/details/82768479 xargs命令    7
# 10-https://blog.csdn.net/qq_41116956/article/details/82767418 关闭防火墙      3

# 11-https://blog.csdn.net/qq_41116956/article/details/82767604 Selinux     4
# 12-https://blog.csdn.net/qq_41116956/article/details/82996319 数据恢复    5
# 13-https://blog.csdn.net/qq_41116956/article/details/82767764 开机挂载    6
# 14-https://blog.csdn.net/qq_41116956/article/details/82768093 本地yum源   5
# 15-https://blog.csdn.net/qq_41116956/article/details/82787400 bash-4.2$问题  7
# 16-https://blog.csdn.net/qq_41116956/article/details/83541818 linux之间NFS文件 6
# 17-https://blog.csdn.net/qq_41116956/article/details/83272420 linux下挂载windows文件 6
# 18-https://blog.csdn.net/qq_41116956/article/details/83272020 linux下挂载U盘
# 19-https://blog.csdn.net/qq_41116956/article/details/84256151 LNMP安装
# 20-https://blog.csdn.net/qq_41116956/article/details/83015312 linux下的find

# 21-https://blog.csdn.net/qq_41116956/article/details/82781270 rm 恢复
# 22-https://blog.csdn.net/qq_41116956/article/details/82788775 root 密码恢复
# 23-https://blog.csdn.net/qq_41116956/article/details/82862900 win查询/kill
# 24-https://blog.csdn.net/qq_41116956/article/details/82851001 linux配置163
# 25-https://blog.csdn.net/qq_41116956/article/details/84775177 docker安装
# 26-https://blog.csdn.net/qq_41116956/article/details/84825963 docker容器篇
# 27-https://blog.csdn.net/qq_41116956/article/details/84838113 docker镜像篇


# 希望刷阅读量的文章的URL
def number():
    url = ['https://blog.csdn.net/qq_41116956/article/details/84105041','https://blog.csdn.net/qq_41116956/article/details/80595285'\
       ,'https://blog.csdn.net/qq_41116956/article/details/80581624','https://blog.csdn.net/qq_41116956/article/details/84105734'\
       ,'https://blog.csdn.net/qq_41116956/article/details/82661381','https://blog.csdn.net/qq_41116956/article/details/82697164'\
       ,'https://blog.csdn.net/qq_41116956/article/details/82767078','https://blog.csdn.net/qq_41116956/article/details/82704365'\
       ,'https://blog.csdn.net/qq_41116956/article/details/82768479','https://blog.csdn.net/qq_41116956/article/details/82767418'\
       #--------------------------------------------------------------------------------------------------------------------------------------
       ,'https://blog.csdn.net/qq_41116956/article/details/82767604','https://blog.csdn.net/qq_41116956/article/details/82996319'\
       ,'https://blog.csdn.net/qq_41116956/article/details/82767764','https://blog.csdn.net/qq_41116956/article/details/82768093'\
       ,'https://blog.csdn.net/qq_41116956/article/details/82787400','https://blog.csdn.net/qq_41116956/article/details/83541818'\
       ,'https://blog.csdn.net/qq_41116956/article/details/83272420','https://blog.csdn.net/qq_41116956/article/details/83272020'\
       ,'https://blog.csdn.net/qq_41116956/article/details/84256151','https://blog.csdn.net/qq_41116956/article/details/83015312'\
       #--------------------------------------------------------------------------------------------------------------------------------------
       ,'https://blog.csdn.net/qq_41116956/article/details/82781270','https://blog.csdn.net/qq_41116956/article/details/82788775'\
       ,'https://blog.csdn.net/qq_41116956/article/details/82862900','https://blog.csdn.net/qq_41116956/article/details/82851001'\
       ,'https://blog.csdn.net/qq_41116956/article/details/84775177','https://blog.csdn.net/qq_41116956/article/details/84825963'\
       ,'https://blog.csdn.net/qq_41116956/article/details/84838113']

    count = 0    # 初始化计数器
    page = []   #页面信息
    # 组装GET方法的请求
    request = []
    for i in range(0,url.__len__()):
        request.append(urllib.request.Request(url[i]))

    while 1:    # 一旦开刷就停不下来
        count += 1    # 计数器加1
        print('开始第%s循环' % count)    # 打印当前循环次数
        for i in range(0,url.__len__()):
            def num():
                rec = urllib.request.urlopen(request[i])  # 发送GET请求，获取博客文章页面资源
                sleep_time = random.randint(50, 60)
                print("正在执行页面：%s 页" % i)
                print('等待时间：%s s' % sleep_time)
                time.sleep(sleep_time)

            if((count%5==0 and i==0) or (count%5==0 and i==1) or (count%6==0 and i==2) or (count%6==0 and i==3) or (count%5==0 and i==4)):
                num()
            if((count%4==0 and i==5) or (count%6==0 and i==6) or (count%6==0 and i==7) or (count%7==0 and i==8) or (count%3==0 and i==9)):
                num()
            if((count%4==0 and i==10) or (count%5==0 and i==11) or (count%6==0 and i==12) or (count%5==0 and i==13) or (count%7==0 and i==14)):
                num()
            if((count%6==0 and i==15) or (count%6==0 and i==16) or (count%8==0 and i==17) or (count%12==0 and i==18) or (count%10==0 and i==19)):
                num()
            if((count%10==0 and i==20) or (count%9==0 and i==21) or (count%10==0 and i==22) or (count%6==0 and i==23) or (count%10==0 and i==24)):
                num()
            if((count%12==0 and i==25) or (count%14==0 and i==26)):
                num()

        sleep_time = random.randint(30,60)
        print('第%s循环完成,等待时间' %count,sleep_time,'s')
        time.sleep(sleep_time)

while 1:
    try:
        number()
    except:
        print("错误！")