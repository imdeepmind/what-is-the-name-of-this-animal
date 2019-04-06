from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense
from keras.applications import MobileNetV2

datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.3)
train_generator = datagen.flow_from_directory('data/dataset/train',
                                                    target_size=(224, 224),
                                                    batch_size=64,
                                                    class_mode='categorical')

test_generator = datagen.flow_from_directory('data/dataset/test',
                                                    target_size=(224, 224),
                                                    batch_size=64,
                                                    class_mode='categorical')

mobile = MobileNetV2(include_top=False,
                          weights="imagenet", 
                          input_shape=(224,224,3),
                          pooling="avg")
model = Sequential()
model.add(mobile)
model.add(Dense(5, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit_transform(train_generator, 
                    epochs=10, 
                    steps_per_epoch=2360/64, 
                    validation_data=test_generator, 
                    validation_steps=263/64)

model.save('data/model.h5')