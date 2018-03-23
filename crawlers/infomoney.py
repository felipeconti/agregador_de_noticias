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
			crLog.openFile("log/infomoney/"+url[1]+"log.txt")

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			newslist = s.find_all('a', {'class':'title-box title-box-medium' )})

			for singlenews in newslist:
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
										"infomoney"
										])
			crLog.closeFile()

	def run(self):

		urls = [['http://www.infomoney.com.br/mercados/ultimas-noticias', 'marcados'],
				['http://www.infomoney.com.br/negocios/ultimas-noticias', 'negocios'],
				['http://www.infomoney.com.br/onde-investir/ultimas-noticias', 'onde-investir'],
				['http://www.infomoney.com.br/minhas-financas/ultimas-noticias', 'minhas-financas'],
				['http://www.infomoney.com.br/franquias/ultimas-noticias', 'franquias'],
				['http://www.infomoney.com.br/carreira/ultimas-noticias', 'carreira']
				]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("www.infomoney.com.br")
		print('---------------------------------------------')

		self.proccess()
		self.commit()
		
		print('---------------------------------------------')


	


	

