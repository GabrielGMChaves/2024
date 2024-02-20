import threading
import cv2
from deepface import DeepFace
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

counter = 0

face_match = False


def analyze_emotion(frame): 
    global face_match
    global objs
    try: 
        objs = DeepFace.analyze(frame, actions = ['emotion','age'])

        if not objs[0] is None:
            face_match = True
        else:
            face_match = False

    except ValueError:
        face_match = False

def put_info_screen():
    cv2.putText(frame, "FACE FOUND!", (20, 450), cv2.FONT_ITALIC, 1, (0, 255, 0), 1)
    dominant_emotion = objs[0]['dominant_emotion']
    age = str(objs[0]['age'])
    cv2.putText(frame, "Emotion: " + dominant_emotion, (20, 45), cv2.FONT_ITALIC, 1, (0, 255, 0), 1)
    cv2.putText(frame, "Age: " + age, (20, 90), cv2.FONT_ITALIC, 1, (0, 255, 0), 1)

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=analyze_emotion, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1    
        
        if face_match:
            put_info_screen()
                        
        else:
            cv2.putText(frame, "NO FACE DETECTED", (20, 450), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
        
        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

    