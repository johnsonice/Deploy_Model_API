#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:44:13 2020

@author: chengyu
"""

import requests 

BASE = 'http://127.0.0.1:5000/'
URL = 'http://modelapi-env.eba-trcyb2gy.us-east-1.elasticbeanstalk.com/api/'
response = requests.get(URL)
print(response.json()['data'])