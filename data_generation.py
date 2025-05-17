import tkinter as tk
from tkinter import messagebox
import cv2
import os
import numpy as np
from PIL import Image
from Data_Collection import generate_dataset
from Train_Model import train_classifier
from Classification import start_recognition

window = tk.Tk()
window.title("Face Recognition System")

#creating label 1
label1 = tk.Label(window, text="Name", font=("Calibri", 20))
label1.grid(column=0, row=0)
t1 = tk.Entry(window, width=50, bd=5)
t1.grid(column=1, row=0)

#creating label 1
label2 = tk.Label(window, text="Age", font=("Calibri", 20))
label2.grid(column=0, row=1)
t2 = tk.Entry(window, width=50, bd=5)
t2.grid(column=1, row=1)

#creating label 1
label3 = tk.Label(window, text="Address", font=("Calibri", 20))
label3.grid(column=0, row=2)
t3 = tk.Entry(window, width=50, bd=5)
t3.grid(column=1, row=2)

#creating buttons
b1 = tk.Button(window, text="Training", font=("Calibri", 20), bg="Blue", fg="White", command=train_classifier)
b1.grid(column=0, row=3)

b2 = tk.Button(window, text="Detect Face", font=("Calibri", 20), bg="Red", fg="White", command=start_recognition)
b2.grid(column=1, row=3)
def gd():
    generate_dataset(t1, t2, t3)

b3 = tk.Button(window, text="Generate Dataset", font=("Calibri", 20), bg="Green", fg="White", command=gd)
b3.grid(column=2, row=3)

window.geometry("800x300")
window.mainloop(0)