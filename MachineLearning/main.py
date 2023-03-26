from cProfile import label
from tokenize import Triple
from black import out
# from unittest import output
from ultralytics import YOLO
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf

IMG_SIZE=50
model = YOLO("yolo_feet_1.pt","v8")
source = "aug127.jpg"
output = model.predict(source= source,save=True)

print(output)
copy=output[0].boxes.boxes
    # apply the cv2.transform to perform matrix transformation
#     # image = cv2.transform(image, m, None)
#     # print(image)
px=pd.DataFrame(copy).astype("float")
px.sort_values(by=[4])
print(px)

v= px.iloc[0,:].to_numpy()
print(v)
k = (v[0],v[1],v[2],v[3])
# # print(W[1])
im = Image.open(source)
im2 = im.crop(k)
# im2.show()
im2=im2.save('middle.png')
# img_feet_gray = im2.convert("L")
# img_feet_gray.show()
threshold = 80
# img_feet_threshold = img_feet_gray.point(lambda x: 255 if x > threshold else 0)
# img_feet_threshold.show()
# img_feet_threshold.save("check.png")
# print(img_feet_threshold)
IMG_SIZE=50
model=tf.keras.models.load_model('82_model.h5')
image = cv2.resize(cv2.imread('middle.png'),(IMG_SIZE,IMG_SIZE))
image = np.array(image)
image=image.reshape(1,50,50,3)
predictions=model.predict(image)
# print(predictions)
k=int(0)
for i in range(0,3):
    if(k<int(predictions[0][i])):
        k = i
for i in range(0,3):
    if (i != k):
        predictions[0][i]=0
    else:
        predictions[0][i]=1


if(predictions[0][0]==1):
    output='FLAT'
elif(predictions[0][1]==1):
    output='NORMAL'
elif(predictions[0][2]==1):
    output='HIGH'
        
    

print(output)