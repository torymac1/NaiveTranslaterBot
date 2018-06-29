#!/usr/bin/env python
# encoding: utf-8

import requests
import json
import os
import tencentsign


def get_content(plus_item, type):
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttrans"
    plus_item = plus_item.encode('utf-8')
    payload = tencentsign.get_params(plus_item, type)
    # r = requests.get(url,params=payload)
    # print(payload)
    try:
        r = requests.post(url, data=payload)
        # print(r.json())
        ret = r.json()

    except:
        ret = {'data': {'trans_text': 'error'}}
    return ret
