import urllib.request
import cv2
import numpy as np

url="http://192.168.1.39:8080/shot.jpg"

while(True):
	imgresp=urllib.request.urlopen(url)
	imgNP=np.array(bytearray(imgresp.read()),dtype=np.uint8)
	img=cv2.imdecode(imgNP,-1)

	cv2.imshow("test",img)
	if ord('q')==cv2.waitKey(10):
		exit(0)
