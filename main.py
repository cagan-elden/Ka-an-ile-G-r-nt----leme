import cv2
import numpy as np

# 0 means first camera, 1 means webcam etc.
cap = cv2.VideoCapture(0)

# Check camera
if not cap.isOpened():
    print("Couldn't open camera")
    exit()

# While the program is running
while True:
    ret, frame = cap.read()

    # If no other frame can be returned break the loop
    if not ret:
        print("Can't recieve frame")
        break

    # Show frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    # When clicked 'q' wait for one second and then break
    if cv2.waitKey(1) == ord('q'):
        break

cap.release() # Stop recording
cv2.destroyAllWindows() # Destroys the page
