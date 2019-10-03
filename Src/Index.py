from flask import Flask, request, jsonify, redirect, url_for, render_template
import os
import json
from Package import initializer
from Package import classifier_train
from Package import test_image
from random import randint
app = Flask(__name__)

TEST_DIR = './Datasets/Test_img'


def initialize():
    obj = initializer.preprocess()
    nrof_images_total, nrof_successfully_aligned = obj.collect_data()
    return


def classify():
    classifier_train.gg()
    return 'Training completed'


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        file = request.files['file']
        img = '/static/Result_img/result_img.jpg'
        f = './Datasets/Test_img/test_img.jpg'
        file.save(f)
        result_output = test_image.test_img(f)
        result = json.loads(result_output)
        return render_template('Test-result.html', result_output=result, file=img)
    return render_template('main_menu.html')


@app.route('/train', methods=['GET', 'POST'])
def train():
    initialize()
    classify()
    return 'The training has been completed'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
