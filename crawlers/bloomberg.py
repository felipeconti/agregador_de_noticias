import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re
from tagfy import tagfy
from crawler import crawler
from newslog import crawlerlog

class crawlerBloomberg(crawler):
	
	def __init__(self):
		crawler.__init__(self)


	def proccess(self):
		for url in self.urls:
			print("Endereço principal -> ", url[0])
			print("")

			crLog = crawlerlog()
			crLog.openFile("log/bloomberg/"+url[1]+"log.txt")

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			newsurl = s.select('h2 a[href]')
			
			for singlenews in newsurl:
				newsurl = singlenews['href']
				article = Article(newsurl)
				article.download()
				try:
					article.parse()
				except:
					print(">>> FALHA NO DOWNLOAD DO LINK <<<")
					print(newsurl)
					continue
				print("Data de publicacao: ", article.publish_date)
				print("Titulo: ", article.title)
				print("Link: ", newsurl)
				print("")

				if not crLog.oldNews(article.title):
					self.save([article.publish_date, 
										newsurl,
										url[0],
										url[1],
										article.title,
										article.text,
										article.authors,
										tagfy(article.title),
										"bloomberg"
									])
			crLog.closeFile()


	def run(self):

		urls = [['https://www.bloomberg.com.br/blog/', 'economia']
			]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("bloomberg.com.br")
		print('---------------------------------------------')

		self.proccess()
		self.commit()
		
		print('---------------------------------------------')

	
