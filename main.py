#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 01:44:43 2021

@author: hedi_bouchelliga
"""
import main_ndf
from Ocr import *
from Ocr import image_to_text

#------------------------------------------------------------------------------
import time
time_start = time.time()
#------------------------------------------------------------------------------

from flask import Flask,request,jsonify,render_template



app = Flask(__name__)
##app.config['SECRET_KEY'] = 'Z\x8a>\xc7R\x18l\xb0\x03\xa9j0\xf4\xfd]\x15.*\xf1\x07\xda\xdep\x10\x04\x16\xba\xa9%\xb1'
# @app.route('/')
# def home():
#     return render_template('index.html')


@app.route("/NDF",methods=["POST"])
def get_informations():
    
#------------------------------------------------------------------------------
    resp = []
    response = []
    image = request.files["image"]
    image_name = image.filename
    image = image.read()

    
#------------------------------------------------------------------------------
    
    
    res = image_to_text.requestOCR('https://vision.googleapis.com/v1/images:annotate', 'AIzaSyDOQ4gFyIPJqwnH5fJselRcMZRA6-hG3dw', image)

#------------------------------------------------------------------------------
    result_dict =  main_ndf.main(res)  
    resp.append(result_dict)    
    #resp = res.json()
    response.append({
        "image name": image_name,
        "informations": resp
        })

#------------------------------------------------------------------------------
    try:
        return jsonify({"response":response}), 200
    except FileNotFoundError:
        abort(404)
        
#------------------------------------------------------------------------------

if __name__ == '__main__':
    #app.run(host = '0.0.0.0', port=5001)
    app.run()
