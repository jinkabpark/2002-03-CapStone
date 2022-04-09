#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CapStone.py
#  
#  2022.04.09  Created by JK.Park
#                Flask Web Server이용 GET, PUT message 처리방법 예시

from flask import Flask
from flask_cors import CORS
from requests.auth import HTTPDigestAuth
from ctypes import *
import sys
import requests

app = Flask(__name__)
app.secret_key = b'ForegnUniversity'
CORS(app)

# hello 수신하고 응답메세지 출력
@app.route("/v1/hello", methods=['GET'])
def home():
    print ('Welcome to UbiFarm !!!')      # for remote test
    return '<h1>Welcome to UbiFarm !!!</h1>'    

# 모터 구동
@app.route('/v1/<objectSequenceNo>', methods=['PUT'])
def operation(objectSequenceNo):
    try:
        sResult = CheckDeviceName(request)          # 실행하기 전에 농장명을 먼저 확인한다
        if sResult == 'fail':
            return 'fail'

        n_RowNo = int(objectSequenceNo)
        sResult = clsSharedLib.OperateObjectsActionNew(n_RowNo, request.json)    # C++ Mixed Program 호출
        if sResult == 'success' :
            print ('call health check in FarmServerNew - success', '\n')
    except Exception as e:
        print ('except in operation at FarmServer', e, '\n')
        return 'fail'        
    return 'success'


if __name__ == "__main__":
    #import NewServer
    app.run(host='0.0.0.0', port=15000, debug=False)
    print ('Flask 기동했습니다 ', '\n')