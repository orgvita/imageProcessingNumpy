import logging
import src.imageProcessingNumpy.tools.config as configas

logging.basicConfig(format=configas.LOG_FORMAT,
                    datefmt=configas.LOG_DATEFMT,
                    level=configas.LOG_LEVEL,
                    filename=configas.LOG_FILE)

logger = logging.getLogger('imageProc')
print(configas.LOG_FILE)