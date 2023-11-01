import ir_datasets
import metapy
dataset = ir_datasets.load("wikir/en1k/training")
with open('queries.txt', 'w+') as f:
	for query in dataset.queries_iter():
		f.write(query.text + '\n')

with open('wikipedia/wikipedia.dat', 'w+') as f:
	for doc in dataset.docs_iter():
		f.write(doc.text + '\n')
