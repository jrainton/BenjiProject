import cv2
import imutils
import glob
import numpy as np
import matplotlib.pyplot as plt

for imageName in glob.glob('*.png'):
    print("New image")
    image = cv2.imread(imageName)
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    cv2.waitKey(0)
    thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)[1]
    #kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
    #thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    #cv2.imshow("Thresh", thresh)
    #cv2.waitKey(0)

    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)

    digitCountours = []
    # loop over the digit area candidates
    for c in contours:
        # compute the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(c)
        string = "This is width: " + str(w) + " and this is height: " + str(h)
        print(string)
        # if the contour is sufficiently large, it must be a digit
        if (50 <= w <= 130) and (30 <= h <= 55):
            digitCountours.append(c)
            roi = image[y:y + h, x:x + w]
            #cv2.imshow("ROI", roi)
            #cv2.waitKey(0)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("contour", image)
    cv2.waitKey(0)