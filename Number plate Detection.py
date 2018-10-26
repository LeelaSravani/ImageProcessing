import cv2
import numpy as np
image = cv2.imread(r"C:\Users\ADMIN\Desktop\My Project\car.jpg")
plate_detect = cv2.CascadeClassifier(r"E:\Anaconda\pkgs\opencv-3.4.1-py36_200\Library\etc\haarcascades\haarcascade_russian_plate_number.xml")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plate = plate_detect.detectMultiScale(gray,1.01,5)
print(plate)
for (x,y,w,h) in plate :
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),5)
cv2.imshow("my plate",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
