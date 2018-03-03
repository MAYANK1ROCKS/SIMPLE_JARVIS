#facerecognition.py
import cv2
import numpy as np
def train(p):
	facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 	
	cam=cv2.VideoCapture(1)
	id=input('enter user id')
	samplenumber=0
	while(True):
		ret,img=cam.read()
		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces=facedetect.detectMultiScale(gray,1.3,5)
		for(x,y,w,h) in faces:
			samplenumber+=1
			cv2.imwrite("dataset/User."+str(id)+"."+str(samplenumber)+".jpg",gray[y:y+h,x:x+w])
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.waitKey(100)
		cv2.imshow("Face",img)
		cv2.waitKey(1)
		if(samplenumber>20):
			break
	
	cam.release()
	cv2.destroyAllWindows()
train(1)
