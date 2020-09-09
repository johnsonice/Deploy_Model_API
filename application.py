#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:36:26 2020

@author: chengyu
"""

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

application = app = Flask(__name__)  #3 for aws beanstock, we need to add application = 
api = Api(app)

class Print_msg(Resource):
    def get(self,name,age):
        return jsonify({"data":
                        {'name':name,
                         'age':age}
                        })  ## it need to be json serializable 
        
class Hello(Resource):
    def get(self):
        return jsonify({"data":"API is working"})  ## it need to be json serializable 
        
## register the api 
api.add_resource(Hello,"/api/")
api.add_resource(Print_msg,"/api/<string:name>/<int:age>")

if __name__=="__main__":
    app.run(debug=True)
    