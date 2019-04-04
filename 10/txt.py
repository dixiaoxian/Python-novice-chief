from urllib import request
from bs4 import BeautifulSoup as bs

zhuyemian = 'http://ggjfwpt.luan.gov.cn'
zy = []
bt=[]

zhuye = ['http://ggjfwpt.luan.gov.cn/laztb/jyxx/002001/002001001/002001001001/','http://ggjfwpt.luan.gov.cn/laztb/jyxx/002001/002001001/002001001003/','http://ggjfwpt.luan.gov.cn/laztb/jyxx/002001/002001001/002001001004/']

resoup = request.urlopen(zhuye[0])
html_date = resoup.read()
soup = bs(html_date,'html.parser')

find_name = soup.find_all('div',class_="ewb-sub")
yemian = (find_name[0].find_all('iframe')[0])['src']
yemian_1 = zhuyemian + yemian

#循环语句
resoup = request.urlopen(yemian_1)
html_date = resoup.read()
soup = bs(html_date,'html.parser')
find_name = soup.find_all('ul')
find_name_1 = (find_name[0].find_all('li'))
for i in find_name_1:
    item = i.find_all('a')
    zy.append(zhuyemian+((item[0])['href']))
    bt.append(((item[0])['title']))

#页面链接+页面标题+页面信息
for i in range(0,zy.__len__() ) :
    print("页面链接："+zy[i])
    print("标题："+bt[i])
    resoup = request.urlopen(zy[i])
    html_date = resoup.read()
    soup = bs(html_date, 'html.parser')
    find_name = soup.find_all('p')
    for i in range(0,find_name.__len__()):
        print(find_name[i].get_text())

#-------------------------------------------------------------------------------------------------------------------------------------------
resoup = request.urlopen(zhuye[1])
html_date = resoup.read()
soup = bs(html_date,'html.parser')


find_name = soup.find_all('ul')
for i in range(0,find_name.__len__()):
    find_name_1 = (find_name[i].find_all('li'))
    for i in find_name_1:
        item = i.find_all('a',class_="ewb-plate-data l")
        # print(item)
        try:
            zy.append(zhuyemian+((item[0])['href']))
            bt.append(((item[0])['title']))
        except Exception as e:
            print('null')



#页面链接+页面标题+页面信息
for i in range(0,zy.__len__() ) :
    # print("页面链接："+zy[i])
    # print("标题："+bt[i])
    resoup = request.urlopen(zy[i])
    html_date = resoup.read()
    soup = bs(html_date, 'html.parser')
    find_name = soup.find_all('p')
    for i in range(0,find_name.__len__()):
        print(find_name[i].get_text())


#-----------------------------------------------------------------------
resoup = request.urlopen(zhuye[2])
html_date = resoup.read()
soup = bs(html_date,'html.parser')

#循环语句
find_name = soup.find_all('ul')
for i in range(0,find_name.__len__()):
    find_name_1 = (find_name[i].find_all('li'))
    for i in find_name_1:
        item = i.find_all('a',class_="ewb-plate-data l")
        try:
            zy.append(zhuyemian+((item[0])['href']))
            bt.append(((item[0])['title']))
        except Exception as e:
            print('null')



#页面链接+页面标题+页面信息
for i in range(0,zy.__len__() ) :
    print("页面链接："+zy[i])
    print("标题："+bt[i])
    resoup = request.urlopen(zy[i])
    html_date = resoup.read()
    soup = bs(html_date, 'html.parser')
    find_name = soup.find_all('p')
    for i in range(0,find_name.__len__()):
        print(find_name[i].get_text())