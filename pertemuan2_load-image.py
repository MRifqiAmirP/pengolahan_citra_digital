import cv2 as cv

img = cv.imread('Gambar/gambar-kucing.jpg', -1)
dimensi =  img.shape

tinggi = img.shape[0]
lebar = img.shape[1]
channels = img.shape[2]

print('Dimensi gambar: ', dimensi)
print('Tinggi gambar: ', tinggi)
print('Lebar gambar: ', lebar)
print('Channel gambar: ', channels)
cv.imshow('Muhammad Rifqi Amir Putra - 5 CA', img)
print(img)

cv.waitKey(0)

cv.destroyAllWindows()