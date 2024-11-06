import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pygltflib import GLTF2

def select_input_folder():
    folder = filedialog.askdirectory(title="Chọn thư mục chứa file .glb")
    if folder:
        input_folder_var.set(folder)

def select_output_folder():
    folder = filedialog.askdirectory(title="Chọn thư mục đầu ra cho file .gltf")
    if folder:
        output_folder_var.set(folder)

def convert_files():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Lỗi", "Vui lòng chọn cả thư mục đầu vào và đầu ra.")
        return

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".glb"):
            input_path = os.path.join(input_folder, filename)

            folder_name = filename.replace(".glb", "")
            folder_path = os.path.join(output_folder, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            output_path = os.path.join(folder_path, folder_name + ".gltf")
            gltf = GLTF2().load(input_path)
            gltf.save(output_path)
            print(f"Đã chuyển đổi: {filename} -> {output_path}")

    messagebox.showinfo("Hoàn tất", "Hoàn tất chuyển đổi tất cả file .glb sang .gltf.")

# Tạo giao diện chính
root = tk.Tk()
root.title("GLB to GLTF Converter")

# Biến lưu trữ đường dẫn thư mục
input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()

# Các thành phần UI
tk.Label(root, text="Thư mục chứa file .glb:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Entry(root, textvariable=input_folder_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Chọn", command=select_input_folder).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Thư mục đầu ra cho file .gltf:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Entry(root, textvariable=output_folder_var, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Chọn", command=select_output_folder).grid(row=1, column=2, padx=5, pady=5)

tk.Button(root, text="Chuyển đổi", command=convert_files, width=20).grid(row=2, column=0, columnspan=3, pady=10)

# Khởi động giao diện
root.mainloop()
