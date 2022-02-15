#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC
@license: None
@contact: JHC000abc@gmail.com
@file: flask_test.py
@time: 2022/1/20 10:23
@desc:
'''
from flask import Flask
from flask_cors import CORS


app=Flask(__name__)
cors = CORS(app, supports_credentials=True)

@app.route('/te',methods=["GET"])
def index():
    return '<h>Hello 112sfgsgsgsgsgdsg22221World!</h>'


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
