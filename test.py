import urllib
import re
import pandas as pd
import pymysql
import os

#爬虫抓取网页函数
def getHtml(url):
    html = urllib.urlopen(url).read()
#     html = html.decode('gbk')
    return html

#抓取网页股票代码函数
def getStackCode(html):
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    return code

Url = 'http://quote.eastmoney.com/stocklist.html'#东方财富网股票数据连接地址
Url = 'http://quote.eastmoney.com/center/gridlist.html'
# filepath = 'D:\\data\\'#定义数据文件保存路径
#实施抓取
code = getStackCode(getHtml(Url)) 
print(code)
# #获取所有股票代码（以6开头的，应该是沪市数据）集合
# CodeList = []
# for item in code:
#     if item[0]=='6':
#         CodeList.append(item)
# #抓取数据并保存到本地csv文件
# for code in CodeList:
#     print('正在获取股票%s数据'%code)
#     url = 'http://quotes.money.163.com/service/chddata.html?code=0'+code+\
#         '&end=20161231&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
#     urllib.request.urlretrieve(url, filepath+code+'.csv')

code='600031'
filepath='/Users/thomas.yuan/Documents/private/StockAnalysis/'
print('正在获取股票%s数据'%code)
url = 'http://quotes.money.163.com/service/chddata.html?code=0'+code+\
'&end=20161231&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
urllib.urlretrieve(url, filepath+code+'.csv')
print(url)