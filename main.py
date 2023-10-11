from loguru import logger
from config import conf
from graph.client import client
from redisgraph import Graph


if __name__ == '__main__':
    logger.info('init redis graph....')
    logger.info('load config')
    if not conf:
        logger.error('load failure')
        exit(1)
    client = client(conf=conf)
    if not client:
        exit(1)
    redis_graph = Graph('SocialGraph', client)
    with open('queries/1.cypher', 'r') as f:
        query = f.read()
    results = redis_graph.query(query)
