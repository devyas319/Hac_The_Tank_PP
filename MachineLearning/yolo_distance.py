from ultralytics import YOLO
import pandas as pd
from PIL import Image

from tqdm import tqdm
import os
model = YOLO("best.pt","v8")
path='dev_leg.jpg'
output = model.predict(path,save=True)
copy=output[0].boxes.boxes
print(copy)
px=pd.DataFrame(copy).astype("float")
print(px)
k = px.iloc[0:3]

kk=int(k[3])
k = int(k[1])

# dist = px.iloc[0:3]-px.iloc[0:1]
print("---------------")
# print(kk-k)
# px.sort_values(by=[4])
v= px.iloc[0,:].to_numpy()
k = (v[0],v[1],v[2],v[3])
im = Image.open(path)
im2 = im.crop(k)

width,hight = im2.size

print(hight)
# os.remove(path)
# im2.save(path)
im2.show()