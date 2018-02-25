from elastic import esCrawler

class crawler():
	def __init__(self):
		urls = []
		self.db = esCrawler()

	def setUrl(self, urls):
		self.urls = urls

	def proccess(self):
		pass

	def commit(self):
		self.db.commit()

	def save(self, doc):
		self.db.save(doc)