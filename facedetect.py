#facerecognition.py
import cv2
import numpy as np
facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cam=cv2.VideoCapture(1)
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainingData.yml")	

#font=cv2.cv.InitFont(cv2.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
	ret,img=cam.read()
	#cv2.putText(img,'OpenCV Tuts!',(10,500), font, 6, (200,255,155), 13, cv2.LINE_AA)
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=facedetect.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		#print(x,y)
		#collecting = cv2.face.StandardCollector.create()
		id,conf=recognizer.predict(gray[y:y+h,x:x+w])
		#print("id:"+str(id))
		name = 'NULL'
		if(id==1):
			name='Mayank Pratap Singh'
		elif(id==2):
			name='Gitesh Khanna'
		elif(id==3):
			name='Abhishek karooti'
		

		#cv2.putText(img,name,(x,y+h), font, 1, (200,255,155), 2, cv2.LINE_AA) #5th para= Size 6th Para = BGRcolor 7th para =Thickness
		cv2.putText(img,name,(x,y+h), font, 1, (0,255,0), 2, cv2.LINE_AA) #5th para= Size 6th Para = BGRcolor 7th para =Thickness
		#cv2.putText(img,str(id),(200,70),font,255,(0,255,0))
		
	cv2.imshow("Face",img)
	if (cv2.waitKey(1)==ord('q')):
		break
cam.release()
cv2.destroyAllWindows()
#recognizer = cv2.face.LBPHFaceRecognizer_create()
