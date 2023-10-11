import redis
from loguru import logger


def client(conf):
    conf = conf.get('redis')
    host = conf.get('host')
    port = int(conf.get('port'))
    password = conf.get('password')
    client = redis.Redis(host=host, port=port, password=password)
    if client.ping():
        logger.info('connection success')
        return client
    else:
        logger.error('connection failed')
        return None
