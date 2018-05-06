from elasticsearch import Elasticsearch
from elasticsearch import helpers


class esCrawler():
	def __init__(self):
		self.es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
		self.news = []

	def save(self, doc):
		self.news.append({
						"_index": "newscenter",
					    "_type": "news",
					    "_source": {
					    	"date":doc[0],
					    	"newslink":doc[1],
					    	"urlorigin":doc[2],
					    	"urlsuborigin":doc[3],
					    	"title":doc[4],
					    	"text":doc[5],
					    	"author":doc[6],
					    	"tags":doc[7],
					    	"provedor":doc[8],
					    }
					})

	def commit(self):
		print(helpers.bulk(self.es, self.news))
		self.news = []
