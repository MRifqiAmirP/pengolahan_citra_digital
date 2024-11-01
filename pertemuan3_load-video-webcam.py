import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv.imshow("Muhammad Rifqi Amir Putra" ,frame)

    key = cv.waitKey(1)
    if key == 27 or key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()