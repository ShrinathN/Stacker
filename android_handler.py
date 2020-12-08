#!/bin/python3

import os
# import numpy as np
import time
import code
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
				return data[i - 1].replace('\n','')

	def get_image_dimensions(self):
		last_image_name = self._get_last_image_name_()
		os.system('adb pull ' + self.IMAGE_DIR + last_image_name)
		time.sleep(1)
		data = cv2.imread(last_image_name)
		# code.interact(local=locals())
		os.system('rm ' + last_image_name)
		return data.shape

	#returns numpy array with data
	def get_latest_image_data(self, ctr):
		last_image_name = self._get_last_image_name_()
		os.system('adb pull ' + self.IMAGE_DIR + last_image_name)
		data = cv2.imread(last_image_name,cv2.IMREAD_COLOR)
		os.system('mv ' + last_image_name + ' ' + str(ctr) + '.jpg')
		# os.system('rm ' + last_image_name)
		return data

	def take_image(self, focus_x=540, focus_y=960):
		#focusing
		os.system('adb shell input touchscreen tap ' + str(focus_x) + ' ' + str(focus_y))
		time.sleep(0.5)
		#clicking image
		os.system('adb shell input touchscreen tap 530 1770')
		time.sleep(2)