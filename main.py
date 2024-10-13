import os
import cv2

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Load background image
imgBackground = cv2.imread('Resources/background.png')

# Path to the folder containing mode images
folderModePath = 'Resources/Modes'
# Get list of mode image paths
modePathList = os.listdir(folderModePath)

# List to hold mode images
imgModeList = []

# Load mode images into imgModeList
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Main loop for capturing video and displaying images
while True:
    success, img = cap.read()
    if not success:
        break

    # Example of overlaying an image (assuming imgModeList[3] exists)
    # You may need additional logic for resizing or positioning
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414]=imgModeList[0]

    # Display the background
    cv2.imshow("Face Attendance", imgBackground)

    cv2.waitKey(1) 