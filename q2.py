
"weaksauce-jk"
from __future__ import print_function

import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time

 
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
#160.0 x 120.0
#176.0 x 144.0
#320.0 x 240.0
#352.0 x 288.0
#640.0 x 480.0
#1024.0 x 768.0
#1280.0 x 1024.0
time.sleep(2)

def decode(im) : 
   
    decodedObjects = pyzbar.decode(im)
   
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')     
    return decodedObjects


font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    
    image=np.zeros((512,512,3),dtype="uint8")
    image[:] = (255,255,255)
   
    ret, frame = cap.read()
    
    cv2.putText(frame,"Challengers",(10,10),cv2.FONT_HERSHEY_DUPLEX,0.5,(110,0,250))
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(2)
    if key & 0xFF == ord('r'):
        b=cv2.imread("w.jpg")
        c=cv2.resize(b,(530,320))
        for i in range(4):
            time.sleep(1)
            ret, frame = cap.read()
           
            im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            im=cv2.resize(im,(530,320))
            cv2.imwrite('4.jpg', im)
            d=cv2.imread("4.jpg")            
            result=cv2.bitwise_and(d,c)
            cv2.imwrite('2.jpg',result)
            c=cv2.imread("2.jpg")
            
            cv2.imshow("image",result)
           
            time.sleep(2)
            i=i+1
        im =cv2.imread("2.jpg")  
        decodedObjects = decode(im)

        for decodedObject in decodedObjects: 
            points = decodedObject.polygon

     
            
            if len(points) > 4 : 
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else : 
                hull = points;
         
           
            n = len(hull)     
           
            for j in range(0,n):
                cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

            x = decodedObject.rect.left
            y = decodedObject.rect.top

            print(x, y)

            print('Type : ', decodedObject.type)
            print('Data : ', decodedObject.data,'\n')
           
            cv2.putText(image,"Code:",(10,200),cv2.FONT_HERSHEY_PLAIN,5,(10,150,250))
            cv2.putText(image,str(decodedObject.data),(10,256),cv2.FONT_HERSHEY_PLAIN,3,(10,150,250))
            cv2.imshow("Myimage",image)
            
    
            
     
    decodedObjects = decode(im)

    for decodedObject in decodedObjects: 
        points = decodedObject.polygon
     
        
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;
         
        
        n = len(hull)     
        
        for j in range(0,n):
          cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

        x = decodedObject.rect.left
        y = decodedObject.rect.top

        print(x, y)

        print('Type : ', decodedObject.type)
        print('Data : ', decodedObject.data,'\n')

        barCode = str(decodedObject.data)
        cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
               
    
    cv2.imshow('frame',frame)
    
    
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'): 
        cv2.imwrite('Capture.png', frame)     


cap.release()
cv2.destroyAllWindows()