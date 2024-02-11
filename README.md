# imageProcessingNumpy
This project offers a straightforward approach to image processing, utilizing NumPy for efficient manipulation and transformation of images.

## Features
ImageProcessingNumpy provides a set of tools for basic image manipulation, including the ability to:
* Crop: Extract the central part of an image.
* Rotate: Rotate images by 90, 180, or 270 degrees.
* Shuffle: Split an image into four parts, shuffle them, and then reassemble to view the shuffled image.
* Resize: Change the size of an image.
* Grayscale Conversion: Convert images to grayscale.
* Save: Persist the transformed image to disk.
* Undo/Reset: Step back through transformations one by one, or revert to the original image at any time.

## To use ImageProcessingNumpy:
1. Clone or Download: First, clone or download the repository to your local machine.
2. Install Python and Dependencies: Ensure you have Python 3.11 installed. Then, install all required dependencies listed in requirements.txt by running pip install -r requirements.txt in your terminal or command prompt.
3. Prepare Your Images:
* By default, the program expects your images to be placed in a "pictures" folder located at the root of the project directory.
* If you wish to use a different folder, please update the relevant paths in config.yaml.
4. Run the Application: Navigate to the project directory in your terminal, and execute python app.py. Follow the on-screen prompts to select an image processing operation.
## Requirements
- Python 3.11
- Modules: numpy, matplotlib, pillow and others (listed in `requirements.txt`)

## Configuration
Configure the application's behavior through config.yaml. Available settings include:
* Logging Level: Adjust the verbosity of application logs.
* Time Intervals: Set how often certain operations are performed.
* Directories: Specify the input and output folders for processing pictures.

## Installation
* Ensure you have Python 3.11 installed
* Dependencies: Dependencies: The project relies on several modules including NumPy, Matplotlib, and Pillow. A complete list of dependencies can be found in requirements.txt.
* Run `pip install -r requirements.txt` to install required modules.

## Extensibility
an GUI version of this program is under way...
