import imageio.v3 as iio

filenames = ['Gambar/Pertemuan 4/img1_1.png', 'Gambar/Pertemuan 4/img2_2.png', 'Gambar/Pertemuan 4/img3_3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('patrick.gif', images, duration=300, loop=0)