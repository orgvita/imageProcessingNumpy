from img_numpy import ImageProcessor
import src.imageProcessingNumpy.tools.config as cfg
from tools.logger import logger

def cli_main():

    while True:
        fname = input("\nEnter the filename (or 'exit' to quit): ")
        if fname.lower() == 'exit':
            break
        original_image = f'{cfg.SOURCE_DIR}{fname}'
        processor = ImageProcessor(original_image)
        logger.info(f'Original image: {original_image}.')
        processor.show_image()
        processor.apply_transformation()


if __name__ == "__main__":
    cli_main()
cli_main()