import cv2
import sys
from time import sleep

# Tell Python where the cascades are
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# This is where we could have some code that takes camera input from the robot
video_capture = cv2.VideoCapture(0)

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1)
    eyes = eyeCascade.detectMultiScale(gray, scaleFactor=1.2)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Draw a rectangle around the eyes
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Test if user input q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# Close everything
video_capture.release()
cv2.destroyAllWindows()