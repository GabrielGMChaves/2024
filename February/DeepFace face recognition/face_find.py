import threading
import cv2
from deepface import DeepFace
import pandas as pd

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

counter = 0

face_match = False

def face_find(frame):
    global face_match
    global objs
    try: 
        objs = DeepFace.find(frame, db_path="./imgs")# place all the images in the imgs folder, it is going to check in the folder which image is the closest from the frame on the webcam
        
        if not objs[0].empty:
            face_match = True
        else:
            face_match = False

    except ValueError:
        face_match = False

def put_info_screen():
    person_name = objs[0]['identity'].apply(lambda x: x.split('/')[-1]).iloc[0]
    x, y, w, h = objs[0][['source_x', 'source_y', 'source_w', 'source_h']].iloc[0]
    cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_ITALIC, 1, (0, 255, 0), 1)
    cv2.putText(frame, f"{person_name}" , (20, 45), cv2.FONT_ITALIC, 1, (0, 255, 0), 1)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)


while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=face_find, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1    
        
        if face_match:
            put_info_screen() 
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_ITALIC, 2, (0, 0, 255), 3)
        
        cv2.imshow("video", frame)
            

    key = cv2.waitKey(1)
    if key == ord("q"):
        break