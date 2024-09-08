import cv2
import numpy as np
import utilities

webcam = False
path = '1.jpg'
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)

    if img is None:
        print("Erro ao carregar a imagem!")
        break

    img = cv2.resize(img, (0, 0), None, 0.3, 0.3)

    img, finalContours = utilities.getContours(img, showCanny=True,
                                               minArea=50000,filter=4)

    if len(finalContours) != 0:
        biggest = finalContours[0][2]
        #print(biggest)
        utilities.WarpImg(img, biggest, 100, 100)

    cv2.imshow('original', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
