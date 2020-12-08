#!/bin/python3

import os
import numpy as np
import cv2

class Device:
	IMAGE_DIR = '/sdcard/DCIM/Camera/'

	def __init__(self):
		os.system('adb wait-for-device')

	def _get_last_image_name_(self):
		os.system('adb shell ls ' + self.IMAGE_DIR + ' > /tmp/files')
		f = open('/tmp/files', 'r')
		data = f.readlines()
		f.close()

		for i in range(0, len(data)):
			if(data[i].find('.mp4') > 0):
				return data[i - 1]


	def get_latest_image_data(self):
		last_image_name = self._get_last_image_name_()
		os.system('adb pull' + self.IMAGE_DIR + last_image_name)
		data = cv2.imread(last_image_name)
		os.system('rm ' + last_image_name)
		return data