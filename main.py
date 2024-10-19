import cv2
import pickle
import numpy as np
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from datetime import datetime
import os
from firebase_admin import db
import time
import threading

# Initialize Firebase credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fare-as-default-rtdb.firebaseio.com/",
    'storageBucket': "fare-as.appspot.com"
})

bucket = storage.bucket()


# Initialize cam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load the larger background image (1280x720)
imgBackground = cv2.imread('Resources/background1.png')

# Check the size of the new background image
print("Background image size:", imgBackground.shape)

# Load known face encodings
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    img = cv2.resize(img, (414, 633))  # Resize to exactly match the placement area
    imgModeList.append(img)

modeType = 0
counter = 0
id = -1
imgStudent = []

# Reduce processing frequency
PROCESS_EVERY_N_FRAMES = 5
frame_count = 0

# Function for database operations
def update_attendance(id):
    try:
        studentInfo = db.reference(f'Students/{id}').get()
        print(f"Student info retrieved: {studentInfo}")  # Debug point 6
        
        if studentInfo:
            datetimeObject = datetime.strptime(studentInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
            secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
            print(f"Seconds elapsed since last attendance: {secondsElapsed}")  # Debug point 7
            
            if secondsElapsed > 30:
                ref = db.reference(f'Students/{id}')
                studentInfo['total_attendance'] += 1
                ref.child('total_attendance').set(studentInfo['total_attendance'])
                ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print(f"Attendance updated for student {id}")  # Debug point 8
            else:
                print(f"Attendance already marked for student {id}")  # Debug point 9
        else:
            print(f"No student info found for ID: {id}")  # Debug point 10
    except Exception as e:
        print(f"Error updating attendance: {e}")

while True:
    start_time = time.time()  # Start timing the loop

    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        continue

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    if len(imgModeList) > 0:
        imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    # Process every Nth frame
    if frame_count % PROCESS_EVERY_N_FRAMES == 0:
        try:
            faceCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
            print(f"Number of faces detected: {len(faceCurFrame)}")  # Debug point 3

            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)
                print(f"Best match index: {matchIndex}, Distance: {faceDis[matchIndex]}")  # Debug point 4

                if matches[matchIndex]:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                    imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                    id = studentIds[matchIndex]
                    print(f"Match found! Student ID: {id}")  # Debug point 5

                    if counter == 0:
                        cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                        cv2.imshow("Face Attendance", imgBackground)
                        cv2.waitKey(1)
                        counter = 1
                        modeType = 1
                        
                        # Start a new thread for database operations
                        threading.Thread(target=update_attendance, args=(id,)).start()

        except Exception as e:
            print(f"Error in face recognition: {e}")

    cv2.imshow("Face Attendance", imgBackground)
    
    # Check for 'q' key press to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_count += 1
    print(f"Current mode: {modeType}, Counter: {counter}")  # Debug point 11

    # Ensure the loop doesn't run faster than 30 FPS
    elapsed_time = time.time() - start_time
    if elapsed_time < 1/30:
        time.sleep(1/30 - elapsed_time)

cap.release()
cv2.destroyAllWindows()

# Add UI enhancements as needed

print(f"Background image shape: {imgBackground.shape}")
for i, img in enumerate(imgModeList):
    print(f"Mode image {i} shape: {img.shape}")
