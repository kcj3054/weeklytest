from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbStock

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/stock', methods=['GET'])
def getStock():

    print(stock);
    return jsonify({'all_stock': stock})

## API 역할을 하는 부분
@app.route('/stock', methods=['POST'])
def save_info():
    info = request.json
    # db.collection.distinct(컬럼명)
    # market, sector, tag

    stock = db.codes.distinct('info')
    ##생략
	return jsonify(stock)

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)