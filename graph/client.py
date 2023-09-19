import redis
from loguru import logger


def client(conf):
    conf = conf.get('redis')
    host = conf.get('host')
    port = int(conf.get('port'))
    password = conf.get('password')
    client = redis.Redis(host=host, port=port, password=password)
    if client.ping():
        logger.info('连接成功')
        return client
    else:
        logger.error('连接失败')
        return None
