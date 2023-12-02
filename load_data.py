import ir_datasets

dataset = ir_datasets.load("wikir/en1k/training")
with open('queries.txt', 'w+') as f:
	for query in dataset.queries_iter():
		f.write(query.text + '\n')

with open('wikipedia/wikipedia.dat', 'w+') as f:
	for doc in dataset.docs_iter():
		f.write(doc.text + '\n')

with open('qrels.txt', 'w+') as f:
	for qrel in dataset.qrels_iter():
		f.write(f'{qrel.query_id} {qrel.doc_id} {qrel.relevance}\n')
