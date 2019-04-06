import keras
import cv2
import urllib

model = keras.models.load_model('data/model.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

def class_to_name(pc):
    if pc == 0: 
        return 'cat'
    elif pc == 1:
        return 'dog'
    elif pc == 2:
        return 'elephant'
    elif pc == 3:
        return 'lion'
    elif pc == 4:
        return 'tiger'
    return 'unknown'
    
while True:
    url = input('Please enter the url of the image: ')
    
    try:
        print('Downloading the image')
        urllib.request.urlretrieve(url, 'data/temp.jpg')
    
        img = cv2.imread('data/temp.jpg', 1)
        if img is not None:    
            img = cv2.resize(img, (224,224))
            
            img = img / 255.0
            img = img.reshape(-1,224,224,3)
            
            pred_class = model.predict_classes(img)
            pred_class_name = class_to_name(pred_class[0])
            
            pred_prob = model.predict(img)
            
            print('\nI\'m {}% confident that this animal is {}'.format(round(pred_prob[0][3], ndigits=3) * 100, pred_class_name))
    
    except Exception as ex:
        print(ex)