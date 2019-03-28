import urllib
import os

animals = ['cat', 'dog', 'lion', 'tiger', 'elephant']

for animal in animals:
    if not os.path.exists('data/images/{}'.format(animal)):
        os.makedirs('data/images/{}'.format(animal))
        
    with open('data/{}.txt'.format(animal)) as txt:
        images = txt.read()
        images = images.split('\n')
        print('--There are total {} {} images'.format(len(images), animal))
        for i in range(len(images)):
            try:
                print('--Downloading {} image number {}--'.format(animal, i))
                urllib.request.urlretrieve(images[i], 'data/images/{}/{}.jpg'.format(animal,i))
            except Exception as ex:
                print('--Something went wrong with the {} image number {} : {}--'.format(animal,i,str(ex)))
                
                
# After downloading the data, we need to manually clean the data
                
