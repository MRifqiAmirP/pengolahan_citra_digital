import numpy as np
import cv2 as cv

# Menentukan canvas
img = np.ones((512, 512, 3), np.uint8)*255

# Menggambar garis
cv.line(img, (256, 256), (128, 128), (255, 0, 0), 5)

# Menggambar segi empat
cv.rectangle(img, (200, 200), (300, 300), (0, 255, 0), -1)

# Menggambar lingkaran
cv.circle(img, (128, 128), 60, (255, 0, 255), -1)

# Menggambar elipse
cv.ellipse(img, (128, 90), (70, 30), 0, 0, 360, (0, 0, 0), 5)

# Menggambar poligon
pts = np.array([[50, 50], [90, 90], [60, 40]], np.int32)
cv.polylines(img, [pts], True, (128, 128, 0), 3)

# Menyisipkan teks
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "Muhammad Rifqi Amir Putra", (10, 500), font, .5, (0, 0, 0), 1, cv.LINE_AA)

cv.imshow("My Drawing", img)
cv.waitKey(0)
cv.destroyAllWindows()