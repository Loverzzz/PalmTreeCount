import os
import cv2

# Path ke folder gambar dan label
image_folder = r"D:\backup\download\house-prices-advanced-regression-techniques\SAWITPRO\dataset\image\val\raw"  # Ganti dengan path ke folder gambar asli
label_folder = r"D:\backup\download\house-prices-advanced-regression-techniques\SAWITPRO\dataset\labels\val"  # Ganti dengan path ke folder label YOLO
output_folder = r"D:\backup\download\house-prices-advanced-regression-techniques\SAWITPRO\dataset\image\val"  # Ganti dengan folder untuk menyimpan gambar annotated

# Buat folder output jika belum ada
os.makedirs(output_folder, exist_ok=True)

# Warna untuk bounding box (BGR format)
bbox_color = (0, 255, 0)  # Hijau
bbox_thickness = 2

# Loop melalui semua file label
for label_file in os.listdir(label_folder):
    if label_file.endswith('.txt'):  # Hanya proses file .txt
        image_file = os.path.splitext(label_file)[0] + ".jpg"  # Asumsikan file gambar format .jpg
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, label_file)

        # Cek apakah gambar ada
        if not os.path.exists(image_path):
            print(f"Gambar tidak ditemukan untuk {label_file}")
            continue

        # Load gambar
        image = cv2.imread(image_path)
        height, width, _ = image.shape

        # Baca file label
        with open(label_path, "r") as f:
            lines = f.readlines()

        # Loop melalui setiap bounding box
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                print(f"Format salah di file {label_file}: {line}")
                continue
            
            # YOLO format: class_id x_center y_center width height
            _, x_center, y_center, box_width, box_height = map(float, parts)

            # Konversi dari normalized ke koordinat pixel
            x_center, y_center = int(x_center * width), int(y_center * height)
            box_width, box_height = int(box_width * width), int(box_height * height)

            # Hitung koordinat sudut kiri atas dan kanan bawah
            x1, y1 = int(x_center - box_width / 2), int(y_center - box_height / 2)
            x2, y2 = int(x_center + box_width / 2), int(y_center + box_height / 2)

            # Gambar bounding box
            cv2.rectangle(image, (x1, y1), (x2, y2), bbox_color, bbox_thickness)

            # Tambahkan label "palmtree" di atas bounding box
            label = "palmtree"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, bbox_color, 1)

        # Simpan gambar annotated ke folder output
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, image)
        print(f"Gambar annotated disimpan: {output_path}")
