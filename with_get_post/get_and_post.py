# -*- coding: utf-8 -*-
################################################################################
#
#
################################################################################
"""
提供给多模的表情搜索

Authors:
Date:    2018/10/29 16:26:45
"""
import sys
# reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
import json
import time
import json
import urllib2
import hashlib
import urllib

import multiprocessing
import time

# study
# 两种方法区调用request库的session：
# import requests
# # method1
# new_session = requests.session()
# new_session.request()
# # method2
# from requests import Session
# Session().request()
# 　
# 区别： 可以从源码对比request.request是基于上下文管理器做的自动关闭session，而session.request基于http长连接sokcet，
# 保留历史请求的状态，这就对依赖于登陆状态的二次请求提供了很便利的途径，居于token，可以借助python
# reflect也就是反射实现token读取，共享

# study:
# python2 有 urllib2, urllib， python3合并两者，起名为 urllib
# urllib urllib2 urllib3 的区别：
# https://blog.csdn.net/jiduochou963/article/details/87564467


# get1 urllib2.Request
MAX_TRIES_TIMES = 10

token_sign = hashlib.md5('zwf').hexdigest()
json_str_val = {}
json_str_val['access_token'] = token_sign
try:
    json_str_val = json.dumps(json_str_val).replace('\'', '\"')

    # print 'data', json_str_val
    json_str_val = json.loads(json_str_val)
except:
    print ('error')

url = 'http://inner.opt'
word = urllib.urlencode(json_str_val)  # 转换成url编码格式(字符串)

newurl = url + "?" + word

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/51.0.2704.103 Safari/537.36"}
tries = 0
for tries in range(MAX_TRIES_TIMES):
    try:
        # 对着两行进行多次重复
        request = urllib2.Request(newurl, headers=headers)
        response = urllib2.urlopen(request)
        break
    except:
        if tries < (MAX_TRIES_TIMES - 1):
            continue
        else:
            print
            "重试超过10次了，还想不想混了。。"
            break
if tries >= MAX_TRIES_TIMES:
    print
    '崩溃出错吧。。'
    exit()


# get2 request.get
# import requests
#
# url=""
# r=requests.get(url)
# info=r.json()
# print(r.status_code)
# print(info)
# assert str(info["resultcode"])=="200"


# get3 request.session().get()
# client = requests.session()
# resp = client.get(url='...')



# post1  urllib2.request
# text_mod = json.dumps(json_str_val)
# header_dict = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
#     "Content-Type": "application/json"}
# url = ''
# req = urllib2.Request(url=url, data=text_mod, headers=header_dict)
# count_lines += 1
#
# # print text_mod
# res = urllib2.urlopen(req)
# res = res.read()
# print(res)


# post2 requests.post
# header_dict = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
#     "Content-Type": "application/json"}
#
# url = '?'
# timestamp = long(time.time()*1000)
# sign = hashlib.md5('uQTngBBXswUkosmO#' + str(timestamp)).hexdigest()
# url = url + 'timestamp=' + str(timestamp) + '&sign=' + sign
# text_mod = {}
# text_mod["data"] = []
# text_mod["data"].append(json_str_val)
# tries = 0
# res = ''
# for tries in range(MAX_TRIES_TIMES):
#     try:
#         r = requests.post(url, json=text_mod, headers=header_dict)
#         res = (r.text)
#         break
#     except:
#         if tries < (MAX_TRIES_TIMES - 1):
#             continue
#         else:
#             print "重试超过10次了，还想不想混了。。"
#             break
# if tries >= MAX_TRIES_TIMES:


# post3 requests.session().post
# header_dict = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
#     'Content-Type': 'application/json'
# }
# list_qingshan = []
# url = ''
# # 第一次跑获取总的页数
# page = 1
# key_input = {"orderEndTime": end_time,
#              "orderStartTime": start_time,
#              "pageIndex": page,
#              "pageSize": 10,
#              "source": source
#              }
# key_input = json.dumps(key_input)
# tries = 0
# res = ''
# page_sum = 0
# for tries in range(MAX_TRIES_TIMES):
#     try:
#         session = requests.session()
#         requ = session.post(url, data=key_input, headers=header_dict)
#         res = requ.text
#         json_result = json.loads(res)
#         page_sum = json_result.get('data', {}).get('totalCount', 0)
#         # 每页10个，求总得页数
#         page_sum = int(math.ceil(int(page_sum) / 10.0))
#         break
#     except:
#         if tries < (MAX_TRIES_TIMES - 1):
#             continue
#         else:
#             print "重试超过10次了，退出吧"
#             break
# if tries >= MAX_TRIES_TIMES:
#     print '崩溃出错, 让RD看下具体问题吧。。'
#     exit()

