import numpy as np
import imageio
import matplotlib.pyplot as plt

# Path ke file gambar
file_path = "C:\\Users\\muham\\Documents\\TUGAS KULIAH SEMESTER 5\\Pengolahan Citra Digital\\kampus.jpg"

# Membaca gambar
image = imageio.imread(file_path)

# Menyiapkan subplot
fig, axs = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle("implementasi program menggunakan python (numpy dan imageio) untuk representasi warna", fontsize=20)

# 2a. Menampilkan channel warna R (Red)
red_channel = image[:, :, 0]
axs[0, 0].imshow(red_channel, cmap='Reds')
axs[0, 0].set_title("2a. Channel Warna R (Red)")
axs[0, 0].axis('off')

# 2b. Menampilkan channel warna G (Green)
green_channel = image[:, :, 1]
axs[0, 1].imshow(green_channel, cmap='Greens')
axs[0, 1].set_title("2b. Channel Warna G (Green)")
axs[0, 1].axis('off')

# 2c. Menampilkan channel warna B (Blue)
blue_channel = image[:, :, 2]
axs[1, 0].imshow(blue_channel, cmap='Blues')
axs[1, 0].set_title("2c. Channel Warna B (Blue)")
axs[1, 0].axis('off')

# 2d. Konversi warna grayscale
grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
axs[1, 1].imshow(grayscale_image, cmap='gray')
axs[1, 1].set_title("2d. Konversi Warna Grayscale")
axs[1, 1].axis('off')

# 2e. Konversi warna threshold (biner)
threshold_value = 128
binary_image = grayscale_image > threshold_value
axs[2, 0].imshow(binary_image, cmap='gray')
axs[2, 0].set_title("2e. Konversi Warna Threshold (Biner)")
axs[2, 0].axis('off')

# Menghilangkan subplot kosong
axs[2, 1].axis('off')

# Menampilkan hasil
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
