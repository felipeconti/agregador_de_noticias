import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re
from tagfy import tagfy
from crawler import crawler
from newslog import crawlerlog

class crawlerUol(crawler):

	def __init__(self):
		crawler.__init__(self)


	def proccess(self):
		for url in self.urls:
			print("Endereço principal -> ", url[0])
			print("")

			crLog = crawlerlog()
			crLog.openFile("log/reuters/"+url[1]+"log.txt")

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			newslist = s.find_all('div', {'class':'headlineMed standalone' )})

			for singlenews in newslist:
				link = singlenews.find_all('a')
				if len(link) > 0:
					newsurl = link[0]['href']
					article = Article(newsurl)
					article.download()
					article.parse()
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
											"reuters"
											])
			crLog.closeFile()

	def run(self):

		urls = [['https://br.reuters.com/news/archive/businessNews?date=today', 'negocios'],
				['https://br.reuters.com/news/archive/domesticNews?date=today', 'brasil'],
				]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("br.reuters.com")
		print('---------------------------------------------')

		self.proccess()
		self.commit()
		
		print('---------------------------------------------')


	


	

