import os, sys, re, subprocess
import numpy as np
import cv2

if __name__ == '__main__':
	cmd = ['./../build/examples/seek-snapshot']
	proc = subprocess.Popen(cmd,
	 stdout=subprocess.PIPE,
	)

	# cv2.namedWindow('seek', cv2.WINDOW_NORMAL)

	_min = 0x7e00
	def minchange(x):
		global _min
		print("min=%s" % x)
		_min = x

	cv2.createTrackbar('min', 'seek', _min, 0xffff, minchange)

	_max = 0x8200
	def maxchange(x):
		global _max
		print("max=%s" % x)
		_max = x

	cv2.createTrackbar('max', 'seek', _max, 0xffff, maxchange)
	k = 100
	try:
		while k > 10:
			data = proc.stdout.read(208*156*2)
			img = np.fromstring(data, dtype='<H').reshape((156, 208))
			img = np.float32(img)

			img -= _min
			img[img<0] = 0
			img /= (_max-_min)

			if 1:
				img = np.rot90(img, 3)
			if k % 20 == 0:
				cv2.imwrite('seek' + str(k), img)
			# key = cv2.waitKey(1)
			k -= 1
			# if key == 113: # q
			# 	break
	except:
		raise
	finally:
		proc.kill()
		proc.wait()