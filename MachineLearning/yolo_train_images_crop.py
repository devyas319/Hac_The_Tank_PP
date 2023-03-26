from ultralytics import YOLO
import pandas as pd
from PIL import Image

from tqdm import tqdm
import os
model = YOLO("yolo_feet_1.pt","v8")
TRAIN_DIR_FLAT='TRAIN_DIR_FLAT'
TRAIN_DIR_NORMAL='TRAIN_DIR_NORMAL'
TRAIN_DIR_HIGH='TRAIN_DIR_HIGH'
train_url = [TRAIN_DIR_FLAT,TRAIN_DIR_NORMAL,TRAIN_DIR_HIGH]
for i in train_url:
    for file_name in tqdm(os.listdir(i)):
        path  = os.path.join(i,file_name)
        output = model.predict(source= path,save=True)
        copy=output[0].boxes.boxes
        px=pd.DataFrame(copy).astype("float")
        px.sort_values(by=[4])
        v= px.iloc[0,:].to_numpy()
        k = (v[0],v[1],v[2],v[3])
        im = Image.open(path)
        im2 = im.crop(k)
        os.remove(path)
        im2.save(path)