# import threading

import os
import cv2
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import ttk


class Trainer:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.path = "Dataset"
        self.i = 0
        if not os.path.exists('./recognizer'):
            os.makedirs('./recognizer')


    def srartTrain(self):

        # our images are located in the dataset folder
        print("[INFO] start processing faces...")
        print("[INFO] processing image {} ,40".format(self.i + 1))


        Ids, faces = self.getImagesWithID(self.path)
        # update the progress variable value

        self.recognizer.train(faces, Ids)

        self.recognizer.save('recognizer/trainingData.yml')
        cv2.destroyAllWindows()
    def getImagesWithID(self,path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
        return np.array(IDs), faces
