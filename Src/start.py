from flask import Flask,render_template,url_for, request, jsonify
from pprint import pprint
from Package import initializer
from Package import classifier_train
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'db'
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)

@app.route('/login',method='POST')
def log:
    

