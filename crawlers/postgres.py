import psycopg2
from datetime import datetime

class postgres:
	error    = 0
	conn     = None
	cur      = None
	commited = 0
	now = datetime.now()

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
			if raw[0] == None:
				raw[0] = str(self.now.year) + '-' + str(self.now.month) + '-' + str(self.now.day)
			self.cur.execute("INSERT INTO news VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)",
							(raw[0], raw[1], raw[2], raw[3], raw[4], raw[5], raw[6], raw[7]))

	def commit(self):
		self.conn.commit()
		self.commited = 1

	def closeConn(self):
		if self.commited == 0:
			self.commit()

		self.cur.close()
		self.conn.close()