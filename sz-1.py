# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url,headers=header) #创建request请求
    response = urllib2.urlopen(request)  #发送request
   # print response.read()
    content = response.read()
    pattern = re.compile(r'<div.*?class="author">.*?<a.*?>.*?<img.*?>(.*?)</a>.*?<div.*?class="content">(.*?)<!--(.*?)-->.*?</div>.*?<div.*?class="stats">.*?<span.*?class="stats-vote">.*?<i.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0],item[3],item[2],item[1]
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

