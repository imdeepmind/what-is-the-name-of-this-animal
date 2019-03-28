import cv2
import os

animals = ['cat', 'dog', 'lion', 'tiger', 'elephant']
default_path = 'data/images/'

for animal in animals:
    images = os.listdir(default_path + animal)
    print('--Processing {} images--'.format(animal))
    for image in images:
        path = default_path + animal + '/' + image
        img = cv2.imread(path, 1)
        if img is not None:
            img = cv2.resize(img, (224,224))
            cv2.imwrite(path, img)