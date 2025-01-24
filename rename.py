import os  

# Path ke folder yang berisi file gambar  
base_path = r'D:\backup\download\house-prices-advanced-regression-techniques\SAWIT PRO\dataset\project\labels'  

# Loop melalui semua file dalam direktori  
for filename in os.listdir(base_path):  
    file_path = os.path.join(base_path, filename)  # Path lengkap ke file  
    if os.path.isfile(file_path):  # Pastikan itu adalah file  
        print(f"Memeriksa file: {filename}")  # Debug: Menunjukkan file yang sedang diproses  
        
        # Pisahkan nama file, menghilangkan bagian angka  
        parts = filename.split('-')  
        if len(parts) > 1:  # Pastikan ada bagian yang ditemukan  
            new_name = '-'.join(parts[1:])  # Ambil semua bagian setelah angka  
            new_file_path = os.path.join(base_path, new_name)  
            
            # Ubah nama file jika nama baru tidak ada  
            if not os.path.exists(new_file_path):  
                os.rename(file_path, new_file_path)  
                print(f"Ditukar: {filename} menjadi {new_name}")  
            else:  
                print(f"File {new_name} sudah ada. Melewatkan penggantian nama.")  
        else:  
            print(f"Tidak ada pemisahan yang valid untuk file: {filename}")  
    else:  
        print(f"{filename} bukan file.")  