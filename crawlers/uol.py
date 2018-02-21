import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re
from postgres import postgres
from tagfy import tagfy
from crawler import crawler

class crawlerUol(crawler):

	def __init__(self):
		crawler.__init__(self)


	def proccess(self):
		for url in self.urls:
			print("Endereço principal -> ", url[0])
			print("")

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			newslist = s.find_all('li')

			for singlenews in newslist:
				link = singlenews.find_all('a', {'class':re.compile(r"click:m_economia_noticias" )})
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

		urls = [['https://economia.uol.com.br/noticias/afp/', 'economia'],
				['https://economia.uol.com.br/noticias/ansa/', 'economia'],
				['https://economia.uol.com.br/noticias/bbc/', 'economia'],
				['https://economia.uol.com.br/noticias/bloomberg/', 'economia'],
				['https://economia.uol.com.br/noticias/estadao-conteudo/', 'economia'],
				['https://economia.uol.com.br/noticias/EFE/', 'economia'],
				['https://economia.uol.com.br/noticias/reuters/', 'economia'],
				['https://economia.uol.com.br/noticias/valor-online/', 'economia']
				]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("uol.com.br")
		print('---------------------------------------------')

		self.setConnection(db)
		self.connect()
		self.proccess()
		
		print('---------------------------------------------')

		self.desconnect()

	


	

