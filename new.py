import cv2
import numpy as np

# Load the background image
imgBackground = cv2.imread('Resources/background1.png')

# Create a copy of the image to draw on
imgCopy = imgBackground.copy()

# Variable to store the current mouse position
current_x, current_y = -1, -1


# Define the mouse callback function to capture coordinates
def update_mouse_position(event, x, y, flags, param):
    global current_x, current_y
    if event == cv2.EVENT_MOUSEMOVE:  # Track mouse movement
        current_x, current_y = x, y  # Update current mouse position
    elif event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        # Draw a red circle at the clicked position (pin)
        cv2.circle(imgCopy, (x, y), 5, (0, 0, 255), -1)  # Draw red pin
        # Draw a black circle at the clicked position (marker)
        cv2.circle(imgCopy, (x, y), 10, (0, 0, 0), -1)  # Draw black marker
        # Print the coordinates to the console
        print(f"Coordinates: ({x}, {y})")


# Create a window to display the image
cv2.namedWindow("Background Image")
cv2.setMouseCallback("Background Image", update_mouse_position)

while True:
    # Make a copy of the background image to draw on
    imgCopy = imgBackground.copy()

    # Draw dashed horizontal lines from the cursor
    for i in range(0, 1280, 10):  # Horizontal line
        if i % 20 == 0:  # Dashed effect
            cv2.line(imgCopy, (i, current_y), (i + 10, current_y), (0, 0, 255), 1)

    # Draw dashed vertical lines from the cursor
    for j in range(0, 720, 10):  # Vertical line
        if j % 20 == 0:  # Dashed effect
            cv2.line(imgCopy, (current_x, j), (current_x, j + 10), (0, 0, 255), 1)

    # Draw the current cursor position as a red circle
    cv2.circle(imgCopy, (current_x, current_y), 5, (0, 0, 255), -1)  # Draw cursor indicator

    # Display the modified image
    cv2.imshow("Background Image", imgCopy)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
