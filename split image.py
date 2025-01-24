import cv2  
import os  
import numpy as np  

def split_image(image_path, output_dir, patch_size=(512, 512), val_size=0.2):  
    # Membaca gambar  
    image = cv2.imread(image_path)  
    
    # Membuat direktori output jika belum ada  
    os.makedirs(output_dir, exist_ok=True)  
    
    height, width, _ = image.shape  
    patches = []  
    
    # Memecah gambar menjadi patch  
    for y in range(0, height - patch_size[1] + 1, patch_size[1]):  
        for x in range(0, width - patch_size[0] + 1, patch_size[0]):  
            patch = image[y:y + patch_size[1], x:x + patch_size[0]]  
            patches.append(patch)  

    # Mengacak urutan patch  
    np.random.shuffle(patches)  

    # Membagi menjadi train dan validation  
    num_val = int(len(patches) * val_size)  
    train_patches = patches[num_val:]  # Train data  
    val_patches = patches[:num_val]     # Validation data  

    # Simpan patch untuk train  
    for i, patch in enumerate(train_patches):  
        cv2.imwrite(os.path.join(output_dir, 'train', f'train{i}.jpg'), patch)  

    # Simpan patch untuk validation  
    for i, patch in enumerate(val_patches):  
        cv2.imwrite(os.path.join(output_dir, 'val', f'val{i}.jpg'), patch)  

# Path ke gambar dan direktori output  
image_path = r"D:\backup\download\house-prices-advanced-regression-techniques\SAWIT PRO\count.jpeg"  # Ganti dengan path gambar Anda  
output_dir = r'D:\backup\download\house-prices-advanced-regression-techniques\SAWIT PRO\dataset'  # Ganti dengan direktori output yang diinginkan  

# Memecah gambar  
split_image(image_path, output_dir)  