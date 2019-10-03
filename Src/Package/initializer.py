from Package.Facenet.preprocess import preprocesses

input_datadir = './Datasets/Train_img'
output_datadir = './Datasets/Intermediate_img'


def preprocess():
    obj = preprocesses(input_datadir, output_datadir)
    #nrof_images_total, nrof_successfully_aligned = obj.collect_data()
    return obj

#print('Total number of images: %d' % nrof_images_total)
#print('Number of successfully aligned images: %d' % nrof_successfully_aligned)
