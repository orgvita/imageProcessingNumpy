from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import random

import src.imageProcessingNumpy.tools.config as conf
from tools.logger import logger

class ImageProcessor:
    def __init__(self, image_path):
        self.original_image = np.array(Image.open(image_path))
        self.image = self.original_image.copy()
        print(type(self.image))
        self.history = [self.original_image.copy()]

    def show_image(self):
        plt.imshow(self.image, cmap='gray' if len(self.image.shape) == 2 else None)
        plt.axis('off')
        plt.show(block=False)  # Display the window, but don't block the console
        plt.pause(5)  # Wait for 5 seconds
        plt.close()

    def crop_center(self):
        # Example crop: numpy array slicing
        self.h, self.w, _ = self.image.shape
        self.image = self.image[((self.h) - (self.h // 2)):((self.h) + (self.h // 2)), ((self.w) - (self.w // 2)):((self.w) + (self.w // 2))]
        self._save_state()

    def rotate_clockwise(self):
        # Example crop: numpy array slicing
        self.image = np.rot90(self.image)
        self._save_state()

    def split_image_into_four(self):
        """Split the image array into four equal parts."""
        self.height, self.width, _ = self.image.shape
        self.mid_height, self.mid_width = self.height // 2, self.width // 2
        self.top_left = self.image[:self.mid_height, :self.mid_width]
        self.top_right = self.image[:self.mid_height, self.mid_width:(2*self.mid_width)]
        self.bottom_left = self.image[self.mid_height:(2*self.mid_height), :self.mid_width]
        self.bottom_right = self.image[self.mid_height:(2*self.mid_height), self.mid_width:(2*self.mid_width)]
        self.parts = [self.top_left, self.top_right, self.bottom_left, self.bottom_right]
        random.shuffle(self.parts)
        return self.parts

    def shuffle(self):
        self.split_image_into_four()
        # random.shuffle(self.parts)
        self.top_half = np.concatenate(self.parts[2:], axis=1)
        self.bottom_half = np.concatenate(self.parts[:2], axis=1)
        self.shuffled_image = np.concatenate([self.top_half, self.bottom_half], axis=0)
        self.image = self.shuffled_image
        self._save_state()

    def resize_image(self):
        coef = int(input("how many times do you want to reduce the size? Input an integer"))
        self.image = self.image[::coef,::coef]
        self._save_state()

    def convert_to_grayscale(self):
        # Weighted grayscale conversion using dot product
        if len(self.image.shape) == 3:  # Check if image is colored
            self.image = np.dot(self.image[...,:3], [0.2989, 0.5870, 0.1140])
        self._save_state()

    def save_image(self):
        timestamp = int(time.time())
        save_path = f"{conf.OUTPUT_DIR}transformed_image_{timestamp}.jpg"
        Image.fromarray(self.image).save(save_path)
        logger.info(f'transformed image: transformed_image_{timestamp}.jpg')
        print(f"Image saved to {save_path}")

    def undo_last_transformation(self):
        if len(self.history) > 1:
            self.history.pop()
            self.image = self.history[-1].copy()
        else:
            print("No previous state to revert to.")

    def reset_to_original(self):
        self.image = self.original_image.copy()
        self.history = [self.image.copy()]

    def _save_state(self):
        self.history.append(self.image.copy())

    def apply_transformation(self):
        while True:
            print("\nChoose a transformation:")
            print("1. Crop center")
            print("2. Rotate clockwise")
            print("3. Shuffle image")
            print("4. Resize")
            print("5. Convert to Grayscale")
            print("6. Save Image")
            print("7. Undo Last Transformation")
            print("8. Reset to Original")
            print("9. Done with transformations")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.crop_center()
            elif choice == "2":
                self.rotate_clockwise()
            elif choice =='3':
                self.shuffle()
            elif choice == "4":
                self.resize_image()
            elif choice == "5":
                self.convert_to_grayscale()

            elif choice == "6":
                self.save_image()
            elif choice == "7":
                self.undo_last_transformation()
            elif choice == "8":
                self.reset_to_original()
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
            self.show_image()
