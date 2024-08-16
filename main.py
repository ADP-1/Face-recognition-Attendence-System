import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

cap.set(3, 1280)  # width
cap.set(4, 720)   # height

while True:
    success, img = cap.read()
    if not success:
        print("Failed to open Webcam")
        break

    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to exit
        break

cap.release()  # release the capture object
cv2.destroyAllWindows()  # close all OpenCV windows

