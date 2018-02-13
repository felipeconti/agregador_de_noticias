import psycopg2

class postgres:
	error    = 0
	conn     = None
	cur      = None
	commited = 0

	def connect(self):
		try:
		    self.conn = psycopg2.connect("dbname='newscenter' user='guilherme' host='localhost' password='123456'")
		except:
		    print("I am unable to connect to the database")
		    self.error = 1

		if self.error == 0:
			self.cur = self.conn.cursor()


	def insertNews(self, data):
		for raw in data:
			self.cur.execute("INSERT INTO news VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)",
							(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))

	def commit(self):
		self.conn.commit()
		self.commited = 1

	def closeConn(self):
		if self.commited == 0:
			self.commit()

		self.cur.close()
		self.conn.close()