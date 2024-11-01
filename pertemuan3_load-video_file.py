import cv2 as cv

cap = cv.VideoCapture("Gambar/estetik-video-resize-854x480.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video sudah selesai diputar.")
        break

    cv.imshow("Muhammad Rifqi Amir Putra", frame)

    key = cv.waitKey(10)
    if key == 27 or key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()





"""
Kecepatan pemutaran video di OpenCV ditentukan oleh nilai parameter dalam fungsi cv.waitKey(). Parameter ini adalah waktu delay dalam milidetik sebelum frame berikutnya ditampilkan. Nilai yang sangat kecil akan menyebabkan video diputar dengan sangat cepat, karena frame ditampilkan tanpa penundaan yang cukup.

Jika kamu ingin memutar video dengan kecepatan normal, kamu perlu mengatur delay di cv.waitKey() sesuai dengan frame rate dari video tersebut. Sebagian besar video memiliki frame rate sekitar 24-30 frame per detik (fps). Untuk menghitung delay yang sesuai, kamu bisa menggunakan rumus berikut:

delay = 1000 / fps

Jadi jika frame rate video adalah 30 fps, delay-nya adalah sekitar 33 milidetik.

Berikut adalah cara mengubah programmu agar video diputar dengan kecepatan yang normal:
1. Temukan frame rate video menggunakan cap.get(cv.CAP_PROP_FPS).
2. Atur delay pada cv.waitKey() berdasarkan frame rate tersebut.

fps = cap.get(cv.CAP_PROP_FPS)
delay = int(1000 / fps)  # Konversi frame rate menjadi delay dalam milidetik

cap.get(cv.CAP_PROP_FPS) digunakan untuk mendapatkan frame rate dari video.
delay = int(1000 / fps) menghitung delay per frame agar sesuai dengan frame rate.
cv.waitKey(delay) memastikan setiap frame ditampilkan dengan jeda yang sesuai agar pemutaran video tetap pada kecepatan normal.

"""