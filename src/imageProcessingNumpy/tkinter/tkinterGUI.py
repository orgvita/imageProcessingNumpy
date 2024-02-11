import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from src.imageProcessingNumpy.tkinter.img_proc import ImageProcessor


class ImageProcessorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Processor")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Calculate desired tkinter size as 4/5 the screen size
        width = screen_width *4 // 5
        height = screen_height *4 // 5
        # Center the tkinter on the screen
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Apply the dimensions and position to the tkinter
        root.geometry(f"{width}x{height}+{x}+{y}")

        # Initialize the image processor without an image
        self.processor = None

        # Image display area
        self.image_label = tk.Label(master)
        self.image_label.pack()

        # Buttons
        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        self.open_button = tk.Button(self.buttons_frame, text="Open Image", command=self.open_image)
        self.open_button.pack(side=tk.LEFT)

        self.crop_button = tk.Button(self.buttons_frame, text="Crop", command=self.crop_image, state=tk.DISABLED)
        self.crop_button.pack(side=tk.LEFT)

        self.resize_button = tk.Button(self.buttons_frame, text="Resize", command=self.resize_image, state=tk.DISABLED)
        self.resize_button.pack(side=tk.LEFT)

        self.grayscale_button = tk.Button(self.buttons_frame, text="Grayscale", command=self.convert_to_grayscale, state=tk.DISABLED)
        self.grayscale_button.pack(side=tk.LEFT)

        self.grayscale_button = tk.Button(self.buttons_frame, text="Shuffle", command=self.shuffle, state=tk.DISABLED)
        self.grayscale_button.pack(side=tk.LEFT)

        self.undo_button = tk.Button(self.buttons_frame, text="Undo", command=self.undo_last_transformation, state=tk.DISABLED)
        self.undo_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.buttons_frame, text="Reset", command=self.reset_to_original, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.buttons_frame, text="Save", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.processor = ImageProcessor(file_path)
            self.display_image(self.processor.image)
            self.enable_buttons()


    def display_image(self, image):
        max_width, max_height = 1200, 800
        orig_width, orig_height = image.size
        scaling_factor = min(max_width / orig_width, max_height / orig_height)

        if scaling_factor < 1:
            display_width = int(orig_width * scaling_factor)
            display_height = int(orig_height * scaling_factor)
            resized_image = image.resize((display_width, display_height), Image.LANCZOS)
        else:
            resized_image = image

        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=self.tk_image)
        self.master.update_idletasks()

    def enable_buttons(self):
        self.crop_button.config(state=tk.NORMAL)
        self.resize_button.config(state=tk.NORMAL)
        self.grayscale_button.config(state=tk.NORMAL)
        self.undo_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)

    def crop_image(self):
        if self.processor:
            self.processor.crop_image()
            self.display_image(self.processor.image)

    def resize_image(self):
        if self.processor:
            self.processor.resize_image()
            self.display_image(self.processor.image)

    def convert_to_grayscale(self):
        if self.processor:
            self.processor.convert_to_grayscale()
            self.display_image(self.processor.image)

    def shuffle(self):
        if self.processor:
            self.processor.shuffle()
            self.display_image(self.processor.image)


    def undo_last_transformation(self):
        if self.processor:
            self.processor.undo_last_transformation()
            self.display_image(self.processor.image)

    def reset_to_original(self):
        if self.processor:
            self.processor.reset_to_original()
            self.display_image(self.processor.image)

    def save_image(self):
        if self.processor:
            self.processor.save_image()


if __name__ == "__main__":
    root = tk.Tk()
    gui = ImageProcessorGUI(root)
    root.mainloop()