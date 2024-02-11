# A Desktop program where you can upload images and add a watermark.

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Watermark App")

        # Create widgets
        self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.canvas = tk.Canvas(master)
        self.canvas.pack()

        self.watermark_button = tk.Button(master, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.config(width=image.width, height=image.height)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

    def add_watermark(self):
        if hasattr(self, 'image_path'):
            image = Image.open(self.image_path)
            image = image.convert('RGBA')
            draw = ImageDraw.Draw(image)
            watermark_text = "Your Watermark Here"

            font = ImageFont.load_default()

            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            position = (image.width - bbox[2], image.height - bbox[3])

            draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))

            output_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                         filetypes=[("PNG files", "*.png")])
            if output_path:
                image.save(output_path)
                messagebox.showinfo("Sucesso", "Marca d'água adicionada com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
