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
			crLog.openFile("log/uol/"+url[1]+"log.txt")

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
											"uol"
											])
			crLog.closeFile()



	def run(self):

		urls = [['https://economia.uol.com.br/noticias/afp/', 'afp'],
				['https://economia.uol.com.br/noticias/ansa/', 'ansa'],
				['https://economia.uol.com.br/noticias/bbc/', 'bbc'],
				['https://economia.uol.com.br/noticias/bloomberg/', 'bloomberg'],
				['https://economia.uol.com.br/noticias/estadao-conteudo/', 'estadao'],
				['https://economia.uol.com.br/noticias/EFE/', 'efe'],
				['https://economia.uol.com.br/noticias/reuters/', 'reuters'],
				['https://economia.uol.com.br/noticias/valor-online/', 'valor']
				]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("uol.com.br")
		print('---------------------------------------------')

		self.proccess()
		self.commit()
		
		print('---------------------------------------------')


	


	

