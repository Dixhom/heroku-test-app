import json
import requests
from flask import Flask, redirect ,request,render_template,jsonify
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

app = Flask(__name__)

@app.route("/")
def check():
    return render_template('templates/index.index')

@app.route('/output', methods=['POST'])
def output():
    # get urls int json format
    allA = int(request.json['allA'])
    allB = int(request.json['allB'])
    CVA = int(request.json['CVA'])
    CVB = int(request.json['CVB'])

    a,b,c,d=chi2_contingency(np.array([[allA,CVA],[allB,CVB]]))

    return_data = {"result":b}
    return jsonify(ResultSet=json.dumps(return_data))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)