import cv2
import numpy as np
import matplotlib.pyplot as plt
import collections
#eye8 roi = frame[650: 850, 400: 600]
#sakshi roi = frame[700: 900, 100: 400]
#anshul_normal = frame[680: 900, 200: 450]
#video1.mp4 = frame[930: 1100, 270: 480]
#dyslexic sakshi,anshul
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#dyslexic
#cap = cv2.VideoCapture("sakshi.mp4")
#cap = cv2.VideoCapture("anshul_dyslexic.mp4")

#non
#cap = cv2.VideoCapture("anshul_normal.mp4")

#cap = cv2.VideoCapture("sakshi.mp4")
    cap = cv2.VideoCapture("anshul_normal.mp4")
ret,frame = cap.read()
eyes = eye_cascade.detectMultiScale(frame)
dict = {}
for (ex,ey,ew,eh) in eyes:
    area = (ew * eh)
    dict[area]=(ex,ey,ew,eh)
dict = collections.OrderedDict(sorted(dict.items(), reverse=True)[:2])
#dict = take(2,dict.items())
for key in dict.keys():
    ex1, ey1, ew1, eh1 = dict[key]
    # cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
    break
print(dict)
list_x=[]
list = []
list_y = []
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    #frame[y:x]
    #eyes = eye_cascade.detectMultiScale(frame)
    '''ex, ey, ew, eh = eyes[0]
    ex1, ey1, ew1, eh1 = eyes[1]
    cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.rectangle(frame, (ex1, ey1), (ex1 + ew, ey1 + eh), (0, 255, 0), 2)'''
    '''dict = {}
    for (ex,ey,ew,eh) in eyes:
        area = (ew * eh)
        dict[area]=(ex,ey,ew,eh)
    dict = collections.OrderedDict(sorted(dict.items(), reverse=True)[:2])
    #dict = take(2,dict.items())
    print(dict)
    for key in dict.keys():
        ex1, ey1, ew1, eh1 = dict[key]
        #cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
        break
'''
    cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
    cv2.imshow("frame",frame)
    roi = frame[ey1+100: (ey1 + eh1)+50, ex1: (ex1 + ew1)]
    rows, cols, _ = roi.shape
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

    _, threshold = cv2.threshold(gray_roi, 70, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (8, 0, 0), 2)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        cv2.circle(roi, (x + int(w/2),y + int(h/2) ), 1, (0, 0, 255), 2)
        list.append((x + int(w/2), y + int(h/2)))
        list_x.append(x + int(w/2))
        list_y.append(y + int(h/2))
        break


    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break

plt.plot(list_y,list_x)
plt.show()
#cap = cv2.VideoCapture("anshul_normal.mp4")
#cap = cv2.VideoCapture("sakshi.mp4")
while True:
    ret, frame = cap.read()
    if ret is False:
        break

    roi = frame[650: 850, 400: 600]

    key = cv2.waitKey(10)
    if key == 27:
        break
    for x,y in list:
        print(x,y)
        cv2.circle(roi, (x,y), 1, (0, 0, 255), 1)
    cv2.imshow("dots", roi)

cv2.destroyAllWindows()