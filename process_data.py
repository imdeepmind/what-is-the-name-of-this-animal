import os
from sklearn.model_selection import train_test_split

animals = ['cat', 'dog', 'lion', 'tiger', 'elephant']

for animal in animals:
    images = os.listdir('data/images/{}'.format(animal))
    
    train, test = train_test_split(images, test_size=0.3)
    
    if not os.path.exists('data/dataset/train/{}'.format(animal)):
        os.makedirs('data/dataset/train/{}'.format(animal))
        
    if not os.path.exists('data/dataset/test/{}'.format(animal)):
        os.makedirs('data/dataset/test/{}'.format(animal))
        
    for image in train:
        os.rename('data/images/{}/{}'.format(animal,image), 'data/dataset/train/{}/{}'.format(animal,image))
        
    for image in test:
        os.rename('data/images/{}/{}'.format(animal,image), 'data/dataset/test/{}/{}'.format(animal,image))