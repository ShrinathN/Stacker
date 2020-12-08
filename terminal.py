#!/bin/python3

import cv2
import numpy as np
import os
import android_handler

IMAGES_TO_MERGE = 50

adev = android_handler.Device()
image_shape = adev.get_image_dimensions()
master_array = np.array([[[0, 0, 0]] * image_shape[1]] * image_shape[0], dtype=np.uint64)

for counter in range(IMAGES_TO_MERGE):
	adev.take_image()
	master_array += adev.get_latest_image_data(counter)
	print(counter)

master_array_u8 = master_array // IMAGES_TO_MERGE
cv2.imwrite('test.png', master_array_u8.astype('uint8'))