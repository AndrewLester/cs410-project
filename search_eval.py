import math
import sys
import time
import metapy
import pytoml


config_file = 'config.toml'
top_results = 10

if __name__ == '__main__':
    index = metapy.index.make_inverted_index(config_file)
    ranker = metapy.index.OkapiBM25(k1=1.5,b=0.75,k3=3.5)
    # ranker = metapy.index.DirichletPrior(0.5)
    eval = metapy.index.IREval(config_file)

    with open(config_file, 'r') as f:
        config = pytoml.load(f)

    query_cfg = config['query-runner']


    start = time.time()
    query_path = query_cfg.get('query-path', 'queries.txt')
    query_start = query_cfg.get('query-id-start', 0)

    query = metapy.index.Document()
    ndcg = 0.0
    num_queries = 0
    print('Running queries')
    with open(query_path) as f:
        for query_num, line in enumerate(f):
            query.content(line.strip())
            results = ranker.score(index, query, top_results)
            ndcg += eval.ndcg(results, query_start + query_num, top_results)
            num_queries+=1
            print(f'{query.content()} ({results[0][1]}):', index.metadata(results[0][0]).get('content')[:100])
            print()
            if num_queries >= 20:
                break

    ndcg /= num_queries

    print(f'MAP: {eval.map()}')

    print(f"NDCG@{top_results}: {ndcg}")
    print(f"Time: {time.time() - start}")
