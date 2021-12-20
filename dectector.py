import numpy as np
import cv2
import imutils
import datetime
#from request import sendImage
  
def gunDetector(ImgUrl:str):   
    gun_cascade = cv2.CascadeClassifier('cascade.xml')
    #camera = cv2.VideoCapture(0)

    
    firstFrame = None
    #gun_exist = False

    print("11111")
    
    def run():
        gun_exist = False
        frame = cv2.imread(f"{ImgUrl}", 0)
        
        frame = imutils.resize(frame, width = 500)

        #gray = np.zeros(frame.shape[:-1], dtype=frame.dtype)
        #for i, img in enumerate(frame):
        #    gray[i] = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        gun = gun_cascade.detectMultiScale(frame,
                                        1.3, 5,
                                        minSize = (100, 100))
        
        if len(gun) > 0:
            gun_exist = True
            
        for (x, y, w, h) in gun:
            
            frame = cv2.rectangle(frame,
                                (x, y),
                                (x + w, y + h),
                                (255, 0, 0), 2)
            roi_gray = frame[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]    
    
    
        #cv2.imshow("Security Feed", frame)
    
        if gun_exist:
            cv2.imwrite("Gun_Detected.jpg", frame)
            #sendImage("Gun.jpg")
            print("guns detected")
        else:
            print("guns NOT detected")
    
    run()
    #camera.release()
    cv2.destroyAllWindows()