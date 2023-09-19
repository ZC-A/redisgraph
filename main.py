from loguru import logger
from config import conf
from graph.client import client
from redisgraph import Node, Edge, Graph, Path


if __name__ == '__main__':
    logger.info('启动redis graph....')
    logger.info('装载配置文件')
    if not conf:
        logger.error('装载失败')
        exit(1)
    client = client(conf=conf)
    if not client:
        exit(1)
    redis_graph = Graph('social', client)
    query = """MATCH (p:person) RETURN p.name"""
    results = redis_graph.query(query)
    for result in results.result_set:
        logger.info(str(result))
