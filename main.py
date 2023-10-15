from loguru import logger
from config import conf
from graph.client import client
from redisgraph import Graph
import manager

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
    #manager.Person_isLocatedIn_City(redis_graph)
    #manager.Person_knows_Person(redis_graph)
    manager.Comment_hasCreator_Person(redis_graph)
