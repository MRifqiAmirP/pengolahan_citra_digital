import numpy as np
import cv2 as cv

# Menentukan canvas
img = np.ones((512, 512, 3), np.uint8)*255

cv.circle(img, (200, 200), 20, (255, 0, 0), -1)

for angle in range(0, 360, 45):
    x_offset = int(60 * np.cos(np.radians(angle)))
    y_offset = int(60 * np.sin(np.radians(angle)))
    cv.circle(img, (200 + x_offset, 200 + y_offset), 30, (147, 20, 255), -1)

cv.rectangle(img, (190, 220), (210, 320), (0, 255, 0), -1)

daun_pts = np.array([[170, 250], [190, 240], [190, 260]], np.int32)
cv.polylines(img, [daun_pts], True, (0, 128, 0), 3)
daun_pts = np.array([[210, 250], [230, 240], [230, 260]], np.int32)
cv.polylines(img, [daun_pts], True, (0, 128, 0), 3)

for x in range(0, 400, 40):
    triangle_pts = np.array([[x, 340], [x + 15, 320], [x + 30, 340]], np.int32)
    cv.fillPoly(img, [triangle_pts], (0, 128, 0))


font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "Muhammad Rifqi Amir Putra", (10, 500), font, .5, (0, 0, 0), 1, cv.LINE_AA)

cv.imshow("My Drawing", img)
cv.waitKey(0)
cv.destroyAllWindows()