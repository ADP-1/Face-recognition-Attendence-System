import cv2

# Initialize cam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load the larger background image (1280x720)
imgBackground = cv2.imread('Resources/background1.png')

# Check the size of the new background image
print("Background image size:", imgBackground.shape)

while True:
    # Read frame from the camera
    success, img = cap.read()

    if not success:
        break

    # Resize webcam image to fit into the available space (625x466)
    imgSmall = cv2.resize(img, (625, 466))  # Resize webcam image to fit within the specified coordinates

    # Insert the webcam feed into the background at the specified position
    imgBackground[171:171 + 466, 62:62 + 625] = imgSmall  # Using the provided coordinates

    # Display the webcam feed and the overlay on the background
    cv2.imshow("Webcam", imgSmall)
    cv2.imshow('Face Attendance', imgBackground)

    # Press 'q' to quit the loop and close the windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
