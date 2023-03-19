import cv2 as cv
import numpy as np
import main

low_H = 0
low_S = 0
low_V = 0
high_H = 0
high_S = 0
high_V = 0

#TODO: wrap in an if statement checking for a target. Make sure that cap is updated every cycle and that that update is actually reflected here
#Also, how to differentiate between cubes? Maybe reference perceived position? 
#
if main.current_pipeline_index == 1:
    ret, frame = main.cap.read()
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    contours, hierarchies = cv.findContours(frame_threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for i in contours:
        M = cv.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.drawContours(frame, [i], -1, (0, 255, 0), 2)
            cv.circle(frame, (cx, cy), 7, (0, 0, 255), -1)#TODO: This stuff is all diagnostic, delete once it is confirmed working
            cv.putText(frame, "center", (cx - 20, cy - 20),
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv.imshow(frame)
        print(f"x: {cx} y: {cy}")
