# -*- coding: utf-8 -*-
import json
import re
import sys
import uuid
import requests
import hashlib
import time
from imp import reload

import time

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '7a6bee787c0b5c74'
APP_SECRET = 'vNeIXd5Ii4cLSrVo1zMheAGPYhJH6F1k'
# APP_KEY = ''
# APP_SECRET = ''


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

def connect():
    with open('./annotation.txt','r',encoding='utf-8') as fp:
        word = fp.readlines()
        for i in word:
            if len(i) > 0:
                # print(i.replace('\n',''))
                q = i

                data = {}
                data['from'] = 'Chinese'
                data['to'] = 'English'
                data['signType'] = 'v3'
                curtime = str(int(time.time()))
                data['curtime'] = curtime
                salt = str(uuid.uuid1())
                signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
                sign = encrypt(signStr)
                data['appKey'] = APP_KEY
                data['q'] = q
                data['salt'] = salt
                data['sign'] = sign
                data['vocabId'] = "您的用户词表ID"

                response = do_request(data)
                contentType = response.headers['Content-Type']
                if contentType == "audio/mp3":
                    millis = int(round(time.time() * 1000))
                    filePath = "合成的音频存储路径" + str(millis) + ".mp3"
                    fo = open(filePath, 'wb')
                    fo.write(response.content)
                    fo.close()
                else:
                    # print(response.text)
                    english = re.findall("translation(.*?)error",response.text)
                    result = str(english).replace('\'','').replace('\"','').replace('[','').replace(':','').replace(']','').replace(',','')
                    # print(result)
                    with open('./tran_result.txt','a',encoding='utf-8')as fp:
                        fp.write(result+'\n')
                    # result = response.json()['web'][0]['value'][0]
                    # print(result)



if __name__ == '__main__':
    connect()
    print('注释翻译成功')

