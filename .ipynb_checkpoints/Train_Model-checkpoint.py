import cv2
import numpy as np
from PIL import Image
import os
from tkinter import messagebox

def train_classifier():
    data_dir = "dataset"
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = [] #empty list
    ids = []

    for image in path:
        img = Image.open(image).convert('L') #convert image to gray scale
        imgNp = np.array(img, 'uint8') #convert image to array
        id = int(os.path.split(image)[1].split('.')[1])
        faces.append(imgNp)
        ids.append(id) 
    ids = np.array(ids)

    #train the classifier and save it
    clf = cv2.face.LBPHFaceRecognizer_create()
    #train classifier 6 times():
    clf.train(faces, ids)
    clf.write('CustomClassifier.xml')
    messagebox.showinfo("Result", "Training done succesfully.")

#train_classifier('data')