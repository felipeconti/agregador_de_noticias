import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re
from postgres import postgres
from tagfy import tagfy
from crawler import crawler

class crawlerValorEconomico(crawler):

	def __init__(self):
		crawler.__init__(self)

	def proccess(self):
		for url in self.urls:
			print("Endereço principal -> ", url[0])
			print("")

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			links = s.find_all('h2', {'class':re.compile(r"^title" )})

			for link in links:
				if len(link) > 0:
					newsurl = link[0]['href']
					article = Article(newsurl)
					article.download()
					article.parse()
					print("Data de publicacao: ", article.publish_date)
					#print("Autores: ", article.authors)
					print("Titulo: ", article.title)
					print("Link: ", newsurl)
					print("")
					#article.text
					
					self.db.insertNews([[article.publish_date, 
										newsurl,
										url[0],
										url[1],
										article.title,
										article.text,
										article.authors,
										tagfy(article.title)
									]])
					self.db.commit()


	def run(self, db):
		urls = [['http://www.valor.com.br/politica', 'politica'],
				['http://www.valor.com.br/financas', 'financas'],
				['http://www.valor.com.br/empresas', 'empresas'],
				['http://www.valor.com.br/agro', 'agronegocio']
				]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("valor.com.br")
		print('---------------------------------------------')

		self.setConnection(db)
		self.connect()
		self.proccess()
		
		print('---------------------------------------------')

		self.desconnect()

