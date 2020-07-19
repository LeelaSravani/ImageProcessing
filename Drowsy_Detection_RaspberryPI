import cv2
from picamera import PiCamera
import time
import io
#/usr/share/opencv/haarcascades
#picture = cv2.imread('image.jpeg')
#picture = cv2.resize(picture,(500,500))
#cv2.imshow('name',picture)

camera =  PiCamera()
num = int(input('No.of images: '))

images = []
names = []
images_detect = []
for i in range(0,num):
    images.append('image{0}.jpeg'.format(i))
    names.append('image{0}'.format(i))
    images_detect.append('image_{0}.jpeg'.format(i))
#print(images)
eye_state = {'Opened':0,'Closed':0}
camera.resolution = (800,600)
camera.start_preview()

for i in range(0,num):
    camera.capture(images[i],resize=(640,480))
    time.sleep(0.10)
    names[i] = cv2.imread(images[i])
    gray = cv2.cvtColor(names[i], cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(r'/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(gray,1.1,5)
    for(x,y,w,h) in face:
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = names[i][y:y+h,x:x+w]
        eye_cascade = cv2.CascadeClassifier(r'/usr/share/opencv/haarcascades/haarcascade_eye.xml')
        cv2.rectangle(names[i],(x,y),(x+w,y+h),(255,0,0),2)
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,15)

        if len(eyes) == 0:
            eye_state['Closed'] = eye_state['Closed'] + 1
        else:
            eye_state['Opened'] = eye_state['Opened'] + 1
            
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imwrite(images_detect[i],names[i])
camera.stop_preview()

closed = eye_state['Closed']
opened = eye_state['Opened']
print 'Closed : ',closed
print 'Opened : ',opened

if(closed>=0) and (closed < int(num*0.2)):
    print 'not drowsy'
elif closed >= int(num*0.2) and closed < int(num*0.4):
    print 'less drowsy'
elif closed >= int(num*0.4) and closed < int(num*0.6):
    print 'moderate'
elif closed >= int(num*0.6) and closed < int(num*0.8):
    print 'more drowsy'
else:
    print 'slept'
