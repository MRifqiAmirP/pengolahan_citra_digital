import cv2 as cv

img1 = cv.imread("Gambar/Pertemuan 6/Manchester_United_FC_Logo.png")
img2 = cv.imread("Gambar/Pertemuan 6/Real_Madrid_CF_Logo.png")

circle = cv.imread("Gambar/Pertemuan 6/circle.png")
star = cv.imread("Gambar/Pertemuan 6/star.png")

ruins = cv.imread("Gambar/Pertemuan 6/ruins.png")
stars = cv.imread("Gambar/Pertemuan 6/stars.png")

add_image =  cv.add(img1, img2)
# blend_image = cv.addWeighted(img1, .5, img2, 1, 0)
# substracted = cv.subtract(star, circle)
# multiply = cv.multiply(ruins, stars)

cv.imshow("Menambahkan Gambar", add_image)

cv.waitKey(0)
cv.destroyAllWindows()