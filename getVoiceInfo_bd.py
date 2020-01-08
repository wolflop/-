# -*- coding:utf-8 -*-
#filename:voiceInfor.py

from aip import AipSpeech
import sys
import json
import base64
import time
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
timer = time.perf_counter
import requests
from urllib import request
import os

APP_ID = '18206180'
API_KEY = 'xGimO8KyFDWlkmndhR0qctbH'
SECRET_KEY = 'IouklBBrw7BSrLX7wFVP7zhQZOlvi0Ta'
#需要识别的文件


CUID  = '123456PYTHON'
#c采样率
RATE = 16000

# 1537 表示识别普通话，使用输入法模型。1536表示识别普通话，使用搜索模型。根据文档填写PID，选择语言及识别模型
DEV_PID = 1536
ASR_URL = 'http://vop.baidu.com/server_api'
SCOPE = 'audio_voice_assistant_get'

# DEV_PID = 8001
# ASR_URL = 'http://vop.baidu.com/pro_api'
# SCOPE = 'brain_enhanced_asr'  # 有此scope表示有收费极速版能力，没有请在网页里开通极速版
# LM_ID = 1234 

class DemoError(Exception):
    pass

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'

def fetch_token():
    params = { 'grant_type': 'client_credentials',
                'client_id': API_KEY,
                'client_secret':SECRET_KEY}

    post_data = urlencode(params)
    post_data = post_data.encode('utf-8')
    proxy_handler = request.ProxyHandler({"http": 'http://' + 'l07920:Lop@123@proxy.h3c.com:8080',
                   "https": 'http://' + 'l07920:Lop@123@proxy.h3c.com:8080'
                   })
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)
    req = Request(TOKEN_URL, post_data)
    f = urlopen(req)
    result_str = f.read()
    result_str = result_str.decode()
    result = json.loads(result_str)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        # print(SCOPE)
        if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
            raise DemoError('scope is not correct')
        print('SUCCESS WITH TOKEN: %s  EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
   
#
def postData(post_data):
    #设置代理
    proxy_handler = request.ProxyHandler({"http": 'http://' + 'l07920:Lop@123@proxy.h3c.com:8080',
                "https": 'http://' + 'l07920:Lop@123@proxy.h3c.com:8080'
                })
    #安装代理
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)    
    req = Request(ASR_URL, post_data.encode('utf-8'))
    req.add_header('Content-Type', 'application/json')
    try:
        begin = timer()
        f = urlopen(req)
        result_str = f.read()
        print ("Request time cost %f" % (timer() - begin))
    except URLError as err:
        print('asr http response http code : ' + str(err.code))
        result_str = err.read()    
    result_str = json.loads(result_str)
    print(result_str['result'])
if __name__=='__main__':
    token = fetch_token()
    files_path = r'D:\python\aip-python-sdk-2.0.0\baidu_ai\public'
    file_list = os.listdir(files_path)
    for file in file_list:
        file_path = os.path.join(files_path, file)
        print(file_path)
        FORMAT = file[-3:]  #文件格式
        with open(file_path, 'rb') as speech_file:                   
            speech_data = speech_file.read()
            length = len(speech_data)
            speech = base64.b64encode(speech_data)#打开的文件进行编码
            speech = str(speech, 'utf-8')
            parmas = {'dev_id': DEV_PID,
            'format': FORMAT,
            'rate': 16000,
            'token': token,
            'cuid': CUID,
            'channel': 1,
            'speech': speech,
            'len': length
                    }
            post_data = json.dumps(parmas, sort_keys=False)
            postData(post_data)
