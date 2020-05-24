import numpy as np
import cv2

img = cv2.imread ("shapes.png",1)

hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Read color
low_red = np.array([161, 155, 84])
hight_red = np.array([179, 255, 255])

mask = cv2.inRange(hsv_img, low_red, hight_red)
red = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("image",img)
cv2.imshow("mask", mask)  # display the color on white
cv2.imshow(" red mask", red)  # display the color on white

if cv2.waitKey(0) &0xFF == ord('q'):
    cv2.destroyAllWindows()