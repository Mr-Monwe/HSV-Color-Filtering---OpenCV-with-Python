#Libraries
import cv2
import numpy as np
#Pipline
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Creating our window
cv2.namedWindow('Output')


def nothing(x):
    pass


# Creating track bar
cv2.createTrackbar('H', 'Output', 0, 180, nothing)
cv2.createTrackbar('S', 'Output', 0, 255, nothing)
cv2.createTrackbar('V', 'Output', 0, 255, nothing)

while (1):

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    ret, frame = cap.read()

    # converting to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get info from track bar and apply to Output
    H = cv2.getTrackbarPos('H', 'Output')
    S = cv2.getTrackbarPos('S', 'Output')
    V = cv2.getTrackbarPos('V', 'Output')

    # Normal masking algorithm
    lower = np.array([H, S, V])
    upper = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    Output = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Output', Output)

cap.release()
cv2.destroyAllWindows()
