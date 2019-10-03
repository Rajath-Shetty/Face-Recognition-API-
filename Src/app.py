from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from flask_pymongo import PyMongo
import bcrypt
import os
from Package import initializer
from Package import classifier_train
from Package import test_image


app = Flask(__name__)

TEST_DIR = './Datasets/Test_img/'
img = os.path.join('/static/Result_img/result_img.jpg')


def initialize():
    obj = initializer.preprocess()
    nrof_images_total, nrof_successfully_aligned = obj.collect_data()
    return


def classify():
    obj = classifier_train.gg()
    return 'Training completed'


app.config["MONGO_DBNAME"] = "users"
app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)


@app.route('/')
def index():
    # if 'username' in session:
     #   return 'You are logged in as ' + session['username']

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            # return redirect(url_for('index'))
            return render_template('loggedin.html', val=request.form['username'])
    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')


@app.route('/train', methods=['GET', 'POST'])
def train():
    initialize()
    classify()
    return 'The training has been completed'


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        return render_template('Test-result.html', result_output=result_output, file=img)
    return render_template('loggedin.html')


@app.route('/test_img', methods=['GET', 'POST'])
def test_img():
    if request.method == 'POST':
        file = request.files['file']
        img = '/static/Result_img/result_img.jpg'
        f = './Datasets/Test_img/test_img.jpg'
        file.save(f)
        result_output = test_image.test_img(f)
        return render_template('Test-result.html', result_output=result_output, file=img)
    return render_template('test_img.html')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
# if bcrypt.checkpw(request.form['pass'], login_user['name']):
