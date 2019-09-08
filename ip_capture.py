import urllib.request
import cv2
import numpy as np
Id = input('enter your id')
url='http://192.168.1.41:8080/shot.jpg'
sampleNum = 0;
while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    sampleNum = sampleNum + 1
    # all the opencv processing is done here
    cv2.imwrite(str("ActiOn") + "_" + str(sampleNum) + ".jpg", img)

    cv2.imshow('test',img)

    if ord('q')==cv2.waitKey(10):
        exit(0)
