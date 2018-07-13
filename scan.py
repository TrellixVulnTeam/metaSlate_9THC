import cv2
import numpy as np

img = cv2.imread('images/slate1.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 5, 3, 0.04)
img[dst>0.01 * dst.max()] = [0, 0, 255]
while (True):
  cv2.imshow('corners', img)
  if cv2.waitKey(1000) & 0xff == ord("q"):
    break
cv2.destroyAllWindows()