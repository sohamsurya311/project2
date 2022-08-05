import numpy as np 
from playsound import playsound 
import cv2  
 
cap = cv2.VideoCapture(0) 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')    
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')    
 
first_read = True 
 
while True: 
    ret, frame = cap.read() 
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3 ,5) 
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),5) 
        roi_gray = gray[y:y+w, x:x+w] 
        roi_color = frame[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5) 
        for (ex, ey, ew, eh) in eyes: 
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5) 
 
    if (len(eyes)>=2): 
        cv2.putText(frame, "Eyes open!", (100,100), cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255),2) 
        '''if(first_read): 
            cv2.putText(frame,"Eye detected", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),2 ) 
        else: 
             cv2.putText(frame, "Eyes open!", (100,100), cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255),2)''' 
    else: 
        if(first_read): 
            cv2.putText(frame, "No eyes detected", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),2) 
        else: 
            print("Blink detected-----") 
            cv2.waitKey(3000) 
            playsound('C:\\Users\\Lenovo\\Music\\buzzer1.wav') 
            first_read=True 
 
    cv2.imshow('frame', frame) 
    a = cv2.waitKey(1) 
    if (a == ord('q')): 
        break 
    elif(a == ord('s') and first_read): 
        first_read = False 
 
cap.release() 
cv2.destroyAllWindows()