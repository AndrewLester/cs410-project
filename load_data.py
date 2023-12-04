import ir_datasets

dataset = ir_datasets.load("wikir/en1k/training")

query_id_to_idx = {}
with open('queries.txt', 'w+') as f:
	for i, query in enumerate(dataset.queries_iter()):
		query_id_to_idx[query.query_id] = i
		f.write(query.text + '\n')

doc_id_to_idx = {}
with open('wikipedia/wikipedia.dat', 'w+') as f:
	for i, doc in enumerate(dataset.docs_iter()):
		doc_id_to_idx[doc.doc_id] = i
		f.write(doc.text + '\n')

with open('qrels.txt', 'w+') as f:
	for qrel in dataset.qrels_iter():
		f.write(f'{query_id_to_idx[qrel.query_id]} {doc_id_to_idx[qrel.doc_id]} {qrel.relevance}\n')
