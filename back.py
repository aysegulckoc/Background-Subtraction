import numpy as np
from cv2 import cv2 as cv
import matplotlib.pyplot as plt

cap = cv.VideoCapture('/Users/aysegulkoc/Movies/3_01.mp4')
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
kernel = np.ones((10, 10), np.uint8)
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
# fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True)
# fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True)
liste = []
while True:
    ret, old_frame = cap.read()
    frame = old_frame[550:850, 250:1150]

    # frame = old_frame[400:760, 639:1111]
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_CLOSE, kernel)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_CLOSE, kernel)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_CLOSE, kernel)

    (h, w) = fgmask.shape
    total_pix = h * w

    # black_pix = np.sum(fgmask == 0)
    white_pix = np.sum(fgmask == 255)

    metric = white_pix / total_pix
    pix_list.append(metric)

    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

plt.plot(pix_list)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

cap.release()
cv.destroyAllWindows()
