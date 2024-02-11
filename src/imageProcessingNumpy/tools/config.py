# LOG_LEVEL = 'INFO'
# LOG_FORMAT = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
# LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
# LOG_FILE = '../../logs/main.log'
#
# SOURCE_DIR = '../../pictures/'
# OUTPUT_DIR = '../../output/'
#
# # additional, not from user-configured yaml
# EXPLAIN_TEXT = '''some text'''

import yaml

# Load the YAML file
with open("../../config.yaml", 'r') as file:
    config_yml = yaml.safe_load(file)

# Accessing data
LOG_LEVEL = config_yml['logging']['level']
LOG_FORMAT = config_yml['logging']['format']
LOG_DATEFMT = config_yml['logging']['datefmt']
LOG_FILE = config_yml['logging']['file']

SOURCE_DIR = config_yml['path']['source']
OUTPUT_DIR = config_yml['path']['output']

# additional, not from user-configured yaml
EXPLAIN_TEXT = '''some text'''

# import configparser
# # Initialize the parser
# config = configparser.ConfigParser()
# # Read the configuration file
# config.read('../../../config.ini')
#
# LOG_LEVEL = config['logging']['level']
# LOG_FORMAT = config['logging']['format']
# LOG_DATEFMT = config['logging']['datefmt']
# LOG_FILE = config['logging']['file']
#
# SOURCE_DIR = config['path']['source']
# OUTPUT_DIR = config['path']['output']
