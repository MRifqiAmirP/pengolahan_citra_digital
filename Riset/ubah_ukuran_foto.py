from PIL import Image

def resize_image(file_path, target_size):
    with Image.open(file_path) as img:
        img_resized = img.resize(target_size)
        img_resized.save(file_path)
        print(f"Gambar berhasil diubah ukurannya menjadi {target_size} dan disimpan kembali di {file_path}")

file_path = 'Gambar\Pertemuan 6\Manchester_United_FC_Logo.png'
target_size = (800, 816)

resize_image(file_path, target_size)
