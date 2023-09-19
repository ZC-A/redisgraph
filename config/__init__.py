import yaml
from loguru import logger

conf = None

try:
    with open('./config/config.yaml', 'r') as f:
        conf = yaml.load(f.read(), Loader=yaml.FullLoader)
except Exception as e:
    logger.error(str(e))
