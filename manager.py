from loguru import logger
import pandas as pd


def random_pick(filepath):
    df = pd.read_csv(filepath, sep='|')
    pick_df = df.sample(20)
    return pick_df


def Person_isLocatedIn_City(graph):
    # 随机读取一些数据来测试 对应 queries/**.cypher文件
    try:
        with open('queries/Person_isLocatedIn_City.cypher', 'r') as f:
            queries = f.read()  # 读取cypher 语句并用后续数据填充
            # 从对应的csv读取数据并随机取样来测试 循环测试
            picks = random_pick('parameters/Person_isLocatedIn_City.csv')

            for i in range(len(picks)):
                query_key = str(picks.iloc[i, 0])
                res = str(picks.iloc[i, 1])
                cur_queries = queries.format(query_key)
                results = graph.query(cur_queries)
                logger.info(results.result_set)
                ans = results.result_set[0][6]  # 根据对应的语句获得最后的下标结果 在cypher中Cityid被作为第7个返回值 则它的对应下标为6
                if ans != res:
                    logger.error('unequal query: Persion_id {} City_id {}'.format(query_key, res))
                logger.info('equal query: Persion_id {} City_id {}'.format(query_key, res))
    except Exception as e:
        logger.error('query failed ' + str(e))

def Person_knows_Person(graph):
    # 随机读取一些数据来测试 对应 queries/**.cypher文件
    try:
        with open('queries/Person_knows_Person.cypher', 'r') as f:
            queries = f.read()  # 读取cypher 语句并用后续数据填充
            picks = random_pick('parameters/Person_knows_Person.csv')
            ans = []

            for i in range(len(picks)):
                query_key = str(picks.iloc[i, 0])
                res = str(picks.iloc[i, 1])
                cur_queries = queries.format(query_key)
                results = graph.query(cur_queries)
                #logger.info(results.result_set)
                ans = [sublist[0] for sublist in results.result_set]    #由于一个节点的knows关系有多个，因此查询到的friendid会有多个
                # print(ans)
                # print(res)
                if res not in ans:  #friendid有多个，此处需确定res在查询到的friendid中
                    logger.error('unequal query: Person_id {} Friend_id {}'.format(query_key, res))
                logger.info('query success: Friend_id {} Friend_Id_Index {}'.format(res, ans.index(res)))

    except Exception as e:
        logger.error('query failed ' + str(e))

def Comment_hasCreator_Person(graph):
    # 随机读取一些数据来测试 对应 queries/**.cypher文件
    try:
        with open('queries/Comment_hasCreator_Person.cypher', 'r') as f:
            queries = f.read()  # 读取cypher 语句并用后续数据填充
            picks = random_pick('parameters/Comment_hasCreator_Person.csv')

            for i in range(len(picks)):
                query_key = str(picks.iloc[i, 0])
                res = str(picks.iloc[i, 1])
                cur_queries = queries.format(query_key)
                results = graph.query(cur_queries)
                logger.info(results.result_set)
                ans = results.result_set[0][0]  # 根据对应的语句获得最后的下标结果 在cypher中Personid被作为第1个返回值 则它的对应下标为0
                if ans != res:
                    logger.error('unequal query: Comment_id {} Person_id {}'.format(query_key, res))
                logger.info('equal query: Comment_id {} Person_id {}'.format(query_key, res))
    except Exception as e:
        logger.error('query failed ' + str(e))

def Comment_isLocatedIn_Country(graph):
    # 随机读取一些数据来测试 对应 queries/**.cypher文件
    try:
        with open('queries/Comment_isLocatedIn_Country.cypher', 'r') as f:
            queries = f.read()  # 读取cypher 语句并用后续数据填充
            # 从对应的csv读取数据并随机取样来测试 循环测试
            picks = random_pick('parameters/Comment_isLocatedIn_Country.csv')

            for i in range(len(picks)):
                query_key = str(picks.iloc[i, 0])
                res = str(picks.iloc[i, 1])
                cur_queries = queries.format(query_key)
                results = graph.query(cur_queries)
                logger.info(results.result_set)
                ans = results.result_set[0][1]  # 根据对应的语句获得最后的下标结果 在cypher中Country被作为第2个返回值 则它的对应下标为1
                if ans != res:
                    logger.error('unequal query: Comment_id {} Country_id {}'.format(query_key, res))
                logger.info('equal query: Comment_id {} Country_id {}'.format(query_key, res))
    except Exception as e:
        logger.error('query failed ' + str(e))