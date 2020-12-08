#!/bin/python3

import numpy as np
import cv2

arr = []
end = 50

for i in range(0, end):
	arr.append(cv2.imread(str(i) + '.jpg'))

final_image = np.array( [[[0,0,0]] * arr[0].shape[1]] * arr[0].shape[0], dtype=np.uint8)

try:
	for i in range(0, final_image.shape[0]):
		for j in range(0, final_image.shape[1]):
			temp_ch0 = [arr[n][i][j][0] for n in range(0, end)]
			temp_ch1 = [arr[n][i][j][1] for n in range(0, end)]
			temp_ch2 = [arr[n][i][j][2] for n in range(0, end)]
			temp_ch0.sort()
			temp_ch1.sort()
			temp_ch2.sort()
			med_ch0 = temp_ch0[end // 2] if(end % 2 == 0) else ((temp_ch0[(end // 2)]) +  (temp_ch0[(end // 2) - 1])) // 2
			med_ch1 = temp_ch1[end // 2] if(end % 2 == 0) else ((temp_ch1[(end // 2)]) +  (temp_ch1[(end // 2) - 1])) // 2
			med_ch2 = temp_ch2[end // 2] if(end % 2 == 0) else ((temp_ch2[(end // 2)]) +  (temp_ch2[(end // 2) - 1])) // 2

			final_image[i][j][0] = med_ch0
			final_image[i][j][1] = med_ch1
			final_image[i][j][2] = med_ch2

		print(i,j)
	cv2.imwrite("median.png", final_image)
except KeyboardInterrupt:
	cv2.imwrite("median.png", final_image)