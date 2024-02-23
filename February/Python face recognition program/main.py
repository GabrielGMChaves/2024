import tkinter as tk
from tkinter import messagebox
import cv2
import PIL.Image, PIL.ImageTk
from deepface import DeepFace

face_match = False

def option1(): 
    global face_match
    global objs
    global person_name
    try: 
        objs = DeepFace.find(frame, db_path="./imgs")
        if not objs[0].empty:
            person_name = objs[0]['identity'].apply(lambda x: x.split('/')[-1]).iloc[0]
            face_match = True
        else:
            face_match = False

    except ValueError:
        face_match = False

def reset_face_match():
    global face_match
    global text
    face_match = False
    text = "User allowed"   

def display_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    if not cap.isOpened():
        messagebox.showerror("Error", "Failed to open webcam.")
        return
    
    def update_webcam():
        global frame
        ret, frame = cap.read()
        if ret:
            if not face_match:
                option1()
                label.after(10, update_webcam)    
            else:
                cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_ITALIC, 1, (0, 255, 0), 1)
                cv2.putText(frame, f"{person_name}" , (20, 45), cv2.FONT_ITALIC, 1, (0, 255, 0), 1)
                label.after(5000, reset_face_match)
                label.after(5010, update_webcam)    
            
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = PIL.Image.fromarray(rgb_image)
            img = PIL.ImageTk.PhotoImage(image=pil_image)
            label.config(image=img)
            label.image = img

    label = tk.Label(frame_webcam)
    label.pack()
    update_webcam()

root = tk.Tk()
root.title("Face detector")

window_width = 2560
window_height = 1440
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

frame_webcam = tk.Frame(root)
frame_webcam.pack(side="top", fill="both", expand=True)

display_webcam()

root.mainloop()
