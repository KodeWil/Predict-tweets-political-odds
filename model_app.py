# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:44:24 2020

@author: Usuario
"""

from flask import request
from flask import jsonify
from flask import Flask
import emulated_pipeline as model
app = Flask(__name__)

@app.route('/model', methods=['POST'])
def politicalOmeter():
    message = request.get_json(force=True)
    tweet = message['tweet']
    response = {
            'polMetric': 'Political odds: ' + str(model.predict_class(tweet)) + "%"
        }
    return jsonify(response)