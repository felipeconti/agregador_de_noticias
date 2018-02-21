class crawler():
	def __init__(self):
		urls = []
		desconnect = False

	def setUrl(self, urls):
		self.urls = urls

	def setConnection(self, db):
		self.db = db

	def connect(self):
		if self.db == None:
			self.db = postgres()
			self.db.connect()
			self.desconnect = True

	def proccess(self):
		pass

	def desconnect(self):
		if self.desconnect == True:
			self.db.closeconn()
