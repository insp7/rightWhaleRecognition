# NOTE: This is just a script to load only the train images from the image dataset. I have used this exact code during many times to load train data. 
# Thought I should separately write this code out incase if I ever use it again for future training, I would just call this method from here.

import os
import numpy as np
import pandas as pd
import cv2

train_csv = pd.read_csv('dataset/train.csv')
train_csv = train_csv[train_csv['Image'] != 'w_7489.jpg'] # image not present, so remove this entry
test_csv = pd.read_csv('dataset/sample_submission.csv')
test_image_names = test_csv['Image']

def load_train_images_to_dataframe(folder_path):
    image_data = []
    files = os.listdir(folder_path)
    counter = 0

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
    
        if file_name not in test_image_names.values:
            counter += 1
            img = cv2.imread(file_path)
            if img is None:
                print(f"Error: Image {file_name} not loaded!")
                continue
            image_data.append(img)

    df = np.array(image_data)
    return df