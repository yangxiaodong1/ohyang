from urllib.parse import urlencode
from urllib.request import Request, urlopen
# import urllib, urllib2, sys
import ssl


host = 'https://dm-101.data.aliyun.com'
path = '/rest/161225/zmxy/api/zhima.credit.antifraud.verify.json'
method = 'POST'
appcode = '你自己的AppCode'
querys = ''
bodys = {}
url = host + path

bodys['address'] = '''杭州市西湖区天目山路266号'''
bodys['bankCard'] = '''20110602436748024138'''
bodys['certNo'] = '''640202199007164686'''
bodys['certType'] = '''IDENTITY_CARD'''
bodys['email'] = '''jnlxhy@alitest.com'''
bodys['imei'] = '''868331011992179'''
bodys['ip'] = '''101.247.161.1'''
bodys['mac'] = '''44-45-53-54-00-00'''
bodys['mobile'] = '''15843991158'''
bodys['name'] = '''牛德华'''
bodys['wifimac'] = '''00-00-00-00-00-E0'''
# post_data = urllib.urlencode(bodys)
post_data = urlencode(bodys)
# request = urllib2.Request(url, post_data)
request = Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
# 根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# response = urllib2.urlopen(request, context=ctx)
response = urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)