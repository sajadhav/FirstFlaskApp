# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:02:05 2019

@author: vRhythms048
"""
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
  
@app.route('/')
def home():
    return render_template('index.html');


if __name__ == '__main__':
    app.run(debug=True)
    
