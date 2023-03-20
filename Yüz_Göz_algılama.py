import cv2
import numpy as np
yuz_kademeleri = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
goz_kademeleri = cv22.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
videoYakala = cv2.VideoCapture(0)
while True:
    ret, videodanGelenResim = videoYakala.read()
    gri = cv2.cvtColor(videodanGelenResim,cv2.COLOR_BGR2GRAY)
    yuzResimleri = yuz_kademeleri.detecMultiScale(gri, 1.1, 6)
    for(x, y, w, h ) in yuzResimleri:
        cv2.rectangle(
            videodanGelenResim, (x,y),(x + w + y + h), (255, 0, 0),2
        )
        roi_gri = gri[y : y + h, x : x + w]
        roi_rekli = videodanGelenResimy[y : y + h, x : x + w]
        gozler = goz_kademeleri.detecMultiScale(roi_gri)
        for(ex, ey, ew, eh) in gozler:
            cv2.rectangle(roi_rekli, (ex, ey), (ex + ew, ey, eh), (0,255,0),2)
    cv2.imshow("img",videodanGelenResim)
    k = cv2.waitKey(30)& 0xFF
    if k == 27:
        break
videoYakala.realese()
cv2.destroyAllWindow()
