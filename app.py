# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:49:25 2023

@author: havoc
"""

from flask import Flask, request, jsonify,render_template
from model import GPT2PPL
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def predict():
    sentence = request.form['input_text']
    gpt2ppl = GPT2PPL()
    results, out = gpt2ppl(sentence)
    return render_template('index.html',out=out)

if __name__== '__main__':
    app.run(debug=True)
