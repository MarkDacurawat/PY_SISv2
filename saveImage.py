import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def open_image():
    global img_path
    img_path = filedialog.askopenfilename()
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((300, 300))  # Resize image to fit in the preview
        img = ImageTk.PhotoImage(img)
        label.configure(image=img)
        label.image = img

def save_image():
    global img_path
    if img_path:
        # Ensure the directory exists
        save_dir = "/images/students"
        os.makedirs(save_dir, exist_ok=True)
        
        # Get the filename from the original image path
        img_name = os.path.basename(img_path)
        save_path = os.path.join(save_dir, img_name)
        
        print("Original Image Path:", img_path)
        print("Save Path:", save_path)
        
        try:
            img = Image.open(img_path)  # Open the original image
            img.save(save_path)
            print("Image saved successfully.")
        except Exception as e:
            print("Error saving image:", e)


root = tk.Tk()
root.title("Image Viewer")

label = tk.Label(root)
label.pack()

btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(side="left", padx=5, pady=5)

btn_save = tk.Button(root, text="Save Image", command=save_image)
btn_save.pack(side="right", padx=5, pady=5)

img_path = None  # Initialize img_path variable

root.mainloop()
