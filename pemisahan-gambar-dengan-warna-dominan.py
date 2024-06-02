import cv2
import numpy as np
import os
import shutil

# membaca gambar query
query_img = cv2.imread("marjan-melon.jpg")

# mengubah gambar menjadi array numpy agar warna dominannya bisa dihitung dan diketahui
query_img_array = np.array(query_img)

# menghitung nilai rata-rata untuk setiap warna (RGB) pada gambar query
mean_r, _, _, _ = cv2.mean(query_img_array[:,:,0])
mean_g, _, _, _ = cv2.mean(query_img_array[:,:,1])
mean_b, _, _, _ = cv2.mean(query_img_array[:,:,2])

# fungsi untuk mengembalikan nama warna dominan berdasarkan nilai RGB
def get_color_name(R, G, B):
    if R > G and R > B:
        return "Merah"
    elif G > R and G > B:
        return "Hijau"
    else:
        return "Biru"

# mendapatkan nama warna dominan pada gambar query dengan fungsi get_color_name
query_color = get_color_name(mean_r, mean_g, mean_b)

# membuat direktori baru untuk menyimpan gambar yang warnanya mirip
output_dir = os.path.join("D:\Pengolahan-Citra\pemisahan-gambar-dengan-warna-dominan", f"gambar_{query_color.lower()}")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# mencari gambar dengan warna dominan yang serupa
folder_path = r"D:\Pengolahan-Citra\pemisahan-gambar-dengan-warna-dominan"
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg"):
        file_path = os.path.join(folder_path, file_name)
        img = cv2.imread(file_path)
        img_array = np.array(img)
        mean_diff_r = abs(mean_r - cv2.mean(img_array[:,:,0])[0])
        mean_diff_g = abs(mean_g - cv2.mean(img_array[:,:,1])[0])
        mean_diff_b = abs(mean_b - cv2.mean(img_array[:,:,2])[0])
        img_color = get_color_name(cv2.mean(img_array[:,:,0])[0], cv2.mean(img_array[:,:,1])[0], cv2.mean(img_array[:,:,2])[0])
        if img_color == query_color:
            # Menyalin gambar ke direktori baru
            shutil.copy(file_path, output_dir)
            print(f"Gambar yang warnanya mirip telah disalin: {file_name}")

print("Proses selesai.")
