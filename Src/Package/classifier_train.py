from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os

from Package.Facenet.classifier import training


def gg():
    datadir = './Datasets/Intermediate_img'
    modeldir = './Model/model_lfw'
    classifier_filename = './Datasets/Gen_classifier/classifier.pkl'
    print("Training Start")
    obj = training(datadir, modeldir, classifier_filename)
    print(obj)
    get_file = obj.main_train()
    print('Saved classifier model to file "%s"' % get_file)

    #sys.exit("All Done")
    return get_file
