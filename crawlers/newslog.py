
class crawlerlog():

	def __init__(self):
		self.fileName = ""
		self.file = None
		self.text = ""
		self.log = []
		self.numOfNews = 50

	def setNumOfNews(self, numOfNews):
		self.numOfNews = numOfNews

	# Abre o arquivo de log
	def openFile(self, fileName):
		self.fileName = fileName
		try:
		    self.file = open(self.fileName, 'r+')
		except IOError:
		    self.file = open(self.fileName, 'w')

		self.readFile()

	# Faz a leitura de todo arquivp
	def readFile(self):
		self.file.seek(0,0)
		self.text = self.file.readline()
		return self.text

	# Escreve no arquivo
	def fileWrite(self, text):
		self.file.write(text)

	# Gera uma lista com todo o conteudo do arquivo de log
	def generateList(self):
		self.log = self.text.split("|")

	# Verifica se é noticia antiga, ou seja, já existe no arquivo de log
	def oldNews(self, title):
		if len(self.log) == 0:
			self.generateList()

		if title in self.log:
			return True
		else:
			self.addToList(title)
			return False

	# Adiciona na lista, sempre mantendo 10 noticias no log
	def addToList(self, title):
		self.log = [title] + self.log
		if len(self.log) > self.numOfNews:
			self.log.pop()

	# Apaga todo conteudo do arquivo
	def truncFile(self):
		self.file.seek(0,0)
		self.file.truncate()

	# Grava as noticias no arquivo
	def recordList(self):
		newStr = ""

		self.truncFile()

		for l in range(len(self.log)):
			if l == len(self.log)-1:
				newStr += self.log[l]
			else:
				newStr += self.log[l]+"|"
		
		self.fileWrite(newStr)

	# Fecha conexão com o arquivo
	def closeFile(self):
		self.recordList()
		self.file.close()



'''
crLog = crawlerlog()
crLog.openFile("teste.txt")
print(crLog.oldNews("blablablateste1"))
print(crLog.oldNews("blablablateste2"))
print(crLog.oldNews("blablablateste3"))
print(crLog.oldNews("blablablateste4"))
print(crLog.oldNews("blablablateste5"))
print(crLog.oldNews("blablablateste6"))
print(crLog.oldNews("blablablateste7"))
print(crLog.oldNews("blablablateste8"))
print(crLog.oldNews("blablablateste9"))
print(crLog.oldNews("blablablateste10"))
print(crLog.oldNews("blablablateste11"))
print(crLog.oldNews("blablablateste12"))
print(crLog.oldNews("blablablateste13"))
print(crLog.oldNews("blablablateste14"))
print(crLog.oldNews("blablablateste15"))
print(crLog.oldNews("blablablateste16"))
print(crLog.oldNews("blablablateste17"))
crLog.closeFile()
'''