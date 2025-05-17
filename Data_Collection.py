import cv2
import os
from tkinter import messagebox
import mysql.connector

def generate_dataset(t1, t2, t3):
    if(t1.get() == "" or t2.get() == "" or t3.get() == ""):
        messagebox.showinfo("Result", "Please fill all details to proceed!")

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    #database connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Authorize_user",
    )
    mycursor = mydb.cursor()

    #set the unique id 
    u_id = 1 #unique id for every person
    mycursor.execute("select * from users")
    result = mycursor.fetchall()
    u_id = 1 #unique id for every person
    for i in result:
        u_id += 1

    name = t1.get()
    age = t2.get()
    address = t3.get()

    insertQuery = "insert into users(id, name, age, address) values(%s, %s, %s, %s)"
    val = (u_id, name, age, address)
    mycursor.execute(insertQuery, val)
    mydb.commit()
    
    # Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Set up the save path
    save_path = os.path.join('dataset')
    
    # Create directory if it does not exist
    os.makedirs(save_path, exist_ok=True)
    
    print("[INFO] Capturing images. Press 's' to save an image, 'q' to quit.")

    count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        
        cv2.imshow('Frame', frame)
        
        key = cv2.waitKey(1)
        
        if key == ord('s'):
            # Save the detected face
            if len(faces) > 0:
                x, y, w, h = faces[0]
                face_img = gray[y:y+h, x:x+w]
                face_img = cv2.resize(face_img, (200, 200))
                file_path = "dataset/user." + str(u_id) + "." + str(count) + ".jpg"
                cv2.imwrite(file_path, face_img)
                print(f"[INFO] Saved image {count}.jpg")
                count += 1
            else:
                print("[WARNING] No face detected.")
        
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()