import math
import sys
import time
import metapy
import pytoml


config_file = 'config.toml'
top_results = 10

rankers = [
    metapy.index.OkapiBM25(k1=5,b=0.75,k3=1.5),
    metapy.index.DirichletPrior(0.75),
    metapy.index.JelinekMercer(),
    metapy.index.PivotedLength(),
]

if __name__ == '__main__':
    index = metapy.index.make_inverted_index(config_file)
    eval = metapy.index.IREval(config_file)
    ranker = rankers[int(sys.argv[1]) if len(sys.argv) > 1 else 0]

    with open(config_file, 'r') as f:
        config = pytoml.load(f)

    query_cfg = config['query-runner']


    start = time.time()
    query_path = query_cfg.get('query-path', 'queries.txt')
    query_start = query_cfg.get('query-id-start', 0)
    
    print(f'Query start: {query_start}')

    query = metapy.index.Document()
    ndcg = 0.0
    num_queries = 0
    # print(eval.f1())
    print('Running queries')
    with open(query_path) as f:
        for query_num, line in enumerate(f):
            if query_num < query_start:
                continue

            query.content(line.strip())
            results = ranker.score(index, query, top_results)
            ndcg += eval.ndcg(results, query_start + query_num, top_results)
            avg_p = eval.avg_p(results, query_num, top_results)
            recall = eval.recall(results, query_num, top_results)
            # print("Query {} average precision: {}".format(query_num + 1, avg_p))
            num_queries+=1
            if len(results) > 0:
                print(f'{query.content()} ({results[0][1]}):', index.metadata(results[0][0]).get('content')[:100])
                print(f'Recall: {recall}')
            print()
            
            if num_queries >= 500:
                break

    ndcg /= num_queries

    print(f'MAP: {eval.map()}')

    print(f"NDCG@{top_results}: {ndcg}")
    print(f"Time: {time.time() - start}")
