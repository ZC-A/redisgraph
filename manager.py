from loguru import logger
import pandas as pd


def random_pick(filepath):
    df = pd.read_csv(filepath, sep='|')
    pick_df = df.sample(20)
    pick = []
    for index, row in pick_df.iterrows():
        pick.append(df.iloc([], row[1]])


def Person_isLocatedIn_City(graph):
    # 随机读取一些数据来测试 对应 queries/**.cypher文件
    try:
        with open('queries/Person_isLocatedIn_City.cypher', 'r') as f:
            queries = f.read()  # 读取cypher 语句并用后续数据填充
            # 从对应的csv读取数据并随机取样来测试 循环测试
            picks = random_pick('parameters/Person_isLocatedIn_City.csv')
            for pick in picks:
                query_key = str(pick[0])
                res = str(pick[1])
                cur_queries = queries.format(query_key)
                results = graph.query(cur_queries)
                logger.info(results.result_set)
                ans = results.result_set[0][6]  # 根据对应的语句获得最后的下标结果 在cypher中Cityid被作为第7个返回值 则它的对应下标为6
                if ans != res:
                    logger.error('unequal query: Persion_id {} City_id {}'.format(query_key, res))
                logger.info('equal query: Persion_id {} City_id {}'.format(query_key, res))
    except Exception as e:
        logger.error('query failed ' + str(e))
