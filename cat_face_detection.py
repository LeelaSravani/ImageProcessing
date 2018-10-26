import cv2
import numpy as np
image = cv2.imread(r"C:\Users\ADMIN\Desktop\My Project\cats.jpg")
face_detect = cv2.CascadeClassifier(r"E:\Anaconda\pkgs\opencv-3.4.1-py36_200\Library\etc\haarcascades\haarcascade_frontalcatface.xml")
#print(image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face = face_detect.detectMultiScale(gray,1.1,5)
print(face)
for (x,y,w,h) in face :
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),5)
    
cv2.imshow("my color image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
