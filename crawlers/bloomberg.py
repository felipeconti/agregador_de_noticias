import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re
from postgres import postgres
from tagfy import tagfy
from crawler import crawler

class crawlerBloomberg(crawler):
	
	def __init__(self):
		crawler.__init__(self)


	def proccess(self):
		for url in self.urls:
			print("Endereço principal -> ", url[0])
			print("")

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			newsurl = s.select('h2 a[href]')
			
			for singlenews in newsurl:
				newsurl = singlenews['href']
				article = Article(newsurl)
				article.download()
				article.parse()
				print("Data de publicacao: ", article.publish_date)
				print("Titulo: ", article.title)
				print("Link: ", newsurl)
				print("")

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

		urls = [['https://www.bloomberg.com.br/blog/', 'economia']
			]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("bloomberg.com.br")
		print('---------------------------------------------')

		self.setConnection(db)
		self.connect()
		self.proccess()
		
		print('---------------------------------------------')

		self.desconnect()

	
