#!/bin/python3

import tkinter as tk
import PIL.Image, PIL.ImageTk
import numpy as np
import cv2

img = cv2.imread('/home/shinu/Desktop/chop_chop.png')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))


root = tk.Tk()
cv = tk.Canvas(root, width=img.shape[1], height=img.shape[0])
cv.pack()

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
cv.create_image(0, 0, image=photo, anchor=tk.NW)

root.mainloop()