import os
from PIL import Image
import pandas as pd
import torch
from tflearn.layers.core import input_data, fully_connected, dropout 
from tflearn.layers.conv import conv_2d,max_pool_2d 
from tflearn.layers.estimator import regression 
from torch.utils.data import Dataset, DataLoader
from torch import nn
from torchvision import transforms
import cv2
import tflearn
import pickle
from tf_cnn import IMG_SIZE
learning_rate = 1e-3
IMG_SIZE=50
# convnet = input_data([None,IMG_SIZE,IMG_SIZE,3],name='inputs')

# convnet = conv_2d(convnet,64,3,activation='relu')
# convent = max_pool_2d(convnet,2)

# convnet = conv_2d(convnet,32,3,activation='relu')
# convent = max_pool_2d(convnet,2)

# convnet = fully_connected(convnet,512,activation='relu')

# convnet = fully_connected(convnet,3,activation='sigmoid')
# convnet = regression(convnet,optimizer='adam',name='targets',learning_rate=learning_rate,loss='binary_crossentropy',metric = 'accuracy')
# model = tflearn.DNN(convnet,tensorboard_dir='log')

# model = model.load('fireVSnature-0.001-6-conv-basic-5.model.data-00000-of-00001')
# op=model.predict('aug12.jpg')
from keras.models import Sequential
from keras.layers import Dense ,Conv2D, Flatten ,MaxPool2D
from keras.models import Sequential, save_model, load_model
import numpy as np
import tensorflow as tf
model_keras = Sequential()
model_keras.add(Conv2D(64,kernel_size=3,padding='same',activation='relu',input_shape=(50,50,3)))
model_keras.add(MaxPool2D(pool_size=(2,2)))
model_keras.add(Conv2D(32,kernel_size=3,padding='same',activation='relu',input_shape=(50,50,3)))
model_keras.add(MaxPool2D(pool_size=(2,2)))

model_keras.add(Flatten())
model_keras.add(Dense(3,activation='sigmoid'))

model_keras.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model_keras.load_weights('81_model.h5')
# model_keras.predict('aug12.jpg')

# model = load_model('test/saved_model', compile = False)
# image = cv2.imread('aug12.jpg')
# image=image.reshape((IMG_SIZE,IMG_SIZE))
# model=tf.keras.models.load_model('test/saved.model')
# pickled_model = torch.load('Dev/Conv.pt')
# image = cv2.resize(cv2.imread('kishan_leg.jpg'),(IMG_SIZE,IMG_SIZE))
# image = np.array(image)
# image=image.reshape(1,50,50,3)
# predictions=pickled_model(image)
# print(predictions)