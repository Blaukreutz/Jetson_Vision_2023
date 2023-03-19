import cv2 as cv
import numpy as np

current_pipeline_index = 0

cam1 = 0
cam2 = 1

cap1 = cv.VideoCapture(cam1)
cap2 = cv.VideoCapture(cam2)