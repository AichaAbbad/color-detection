import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _ , frame = cap.read()

    cv2.imshow("frame", frame)
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Read color
    low_red= np.array ([161,155,84])
    hight_red = np.array([179, 255, 255])

    mask = cv2.inRange(hsv_frame, low_red, hight_red)
    red = cv2.bitwise_and(frame, frame, mask = mask)

    #cv2.imshow("frame",frame) # display original frame
    cv2.imshow("mask", mask) # display the color on white
    cv2.imshow(" red mask", red) # display the color on white

    if cv2.waitKey(1) &0xFF == ord('q'):
        break