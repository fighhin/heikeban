#coding:utf-8
import requests
import re

url='http://www.heibanke.com/lesson/crawler_ex00/'
reg=r'数字[^\d]*(\d+)[\.<]'

html=requests.get(url).content
item=re.compile(reg,re.S).findall(html)

index=1
while item:
    url1=url+item[0]
    html=requests.get(url1).content
    item=re.compile(reg,re.S).findall(html)
    print '第%d次输入%s'%(index,url1)
    index+=1
else:
    print '最后一次为：%s'%url1



