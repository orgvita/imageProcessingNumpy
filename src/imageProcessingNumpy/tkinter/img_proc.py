from PIL import Image
import time

class ImageProcessor:
    def __init__(self, image_path):
        self.original_image = Image.open(image_path)
        self.image = self.original_image.copy()
        # self.history = [self.image.copy()]
        self.history = [self.original_image]


    def show_image(self):
        if self.image:
            self.image.show()

    def crop_image(self):
        self.image = self.image.crop((100, 100, 400, 400))  # Example crop
        self._save_state()

    def resize_image(self):
        self.image = self.image.resize((200, 200))
        self._save_state()

    def convert_to_grayscale(self):
        self.image = self.image.convert("L")
        self._save_state()

    def save_image(self):
        timestamp = int(time.time())
        save_path = f"../../../output/transformed_image_{timestamp}.jpg"
        self.image.save(save_path)
        logger.info(f'transformed image: transformed_image_{timestamp}.jpg')
        print(f"Image saved to {save_path}")

    def undo_last_transformation(self):
        if len(self.history) > 1:
            self.history.pop()  # Remove the current state
            self.image = self.history[-1].copy()  # Revert to the previous state
        else:
            print("No previous state to revert to.")

    def reset_to_original(self):
        self.image = self.original_image.copy()
        self.history = [self.image.copy()]

    def _save_state(self):
        """Internal method to save the current state of the image."""
        self.history.append(self.image.copy())

    def apply_transformation(self):
        while True:
            print("\nChoose a transformation:")
            print("1. Crop")
            print("2. Resize")
            print("3. Convert to Grayscale")
            print("4. Save Image")
            print("5. Undo Last Transformation")
            print("6. Reset to Original")
            print("7. Done with transformations")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.crop_image()
            elif choice == "2":
                self.resize_image()
            elif choice == "3":
                self.convert_to_grayscale()
            elif choice == "4":
                self.save_image()
            elif choice == "5":
                self.undo_last_transformation()
            elif choice == "6":
                self.reset_to_original()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
            self.show_image()
