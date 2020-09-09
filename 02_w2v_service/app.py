#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:36:26 2020

@author: chengyu
"""

root = '..'

import os,sys
sys.path.insert(0,os.path.join(root,'libs'))
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from w2v import W2V

w2v_path = os.path.join(root,'Data/model_weights/IMF_W2V/imf_160.w2v')
#%%

application = app = Flask(__name__)  #3 for aws beanstock, we need to add application = 
api = Api(app)
 
class Hello(Resource):
    def get(self):
        return jsonify({"data":"API is working"})  ## it need to be json serializable 


w2v = W2V(w2v_path)
class Get_sim_words(Resource):
    def get(self,word,topn):
        if topn is None: topn = 10
        res = w2v.get_most_similar(word,topn=topn)
        return jsonify({"data":
                        {'keyword':word,
                         'sim_words':res}
                        })  ## it need to be json serializable 
## register the api 
api.add_resource(Hello,"/api/")
api.add_resource(Get_sim_words,"/api/getsim/<string:word>/<int:topn>")

if __name__=="__main__":
    app.run(debug=True)
    