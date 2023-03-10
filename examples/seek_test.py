import os, sys, re, subprocess

if __name__ == '__main__':
	cmd = ['./../build/examples/seek-test']
	proc = subprocess.Popen(cmd)

	# cv2.namedWindow('seek', cv2.WINDOW_NORMAL)

	_min = 0x7e00
	def minchange(x):
		global _min
		print("min=%s" % x)
		_min = x

	# cv2.createTrackbar('min', 'seek', _min, 0xffff, minchange)

	_max = 0x8200
	def maxchange(x):
		global _max
		print("max=%s" % x)
		_max = x

	# cv2.createTrackbar('max', 'seek', _max, 0xffff, maxchange)
	k = 100
	try:
		while k > 10:
			data = proc.stdout.read(208*156*2)
			print(data)
			k -= 1
			
	except:
		raise
	finally:
		proc.kill()
		proc.wait()
