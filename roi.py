from cv2 import cv2

'''
For images:
img = cv2.imread("ornek.png")
img_crop = img[583:1290, 750:1350]
'''

cap = cv2.VideoCapture('/Users/aysegulkoc/Movies/2_01.mp4')

while True:
    ret, old_frame = cap.read()
    frame = old_frame[595:850, 200:1150]
    # frame = old_frame[639:623, 1081:1082] --> 2_01.mp4
    cv2.circle(frame, (430, 80), 20, (0, 0, 255), -1)

    cv2.imshow('Frame', frame)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

# cv2.imshow("Normal image", img)
cv2.destroyAllWindows()
