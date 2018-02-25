import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re
from tagfy import tagfy
from crawler import crawler
from newslog import crawlerlog

class crawlerValorEconomico(crawler):

	def __init__(self):
		crawler.__init__(self)

	def proccess(self):
		for url in self.urls:
			print("Endereço principal -> ", url[0])
			print("")

			crLog = crawlerlog()
			crLog.openFile("log/valor/"+url[1]+"log.txt")
			crLog.setNumOfNews(20)

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			links = s.find_all('h2', {'class':re.compile(r"^title" )})
			
			for link in links:
				if len(link) > 0:
					aTag = link.find_all('a')
					if len(aTag) > 0:
						newsurl = aTag[0]['href']
					else:
						continue

					article = Article(newsurl)
					article.download()
					try:
						article.parse()
					except:
						print(">>> FALHA NO DOWNLOAD DO LINK <<<")
						print(link)
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
											"valoreconomico"
										])
			crLog.closeFile()


	def run(self):
		urls = [['http://www.valor.com.br/politica', 'politica'],
				['http://www.valor.com.br/financas', 'financas'],
				['http://www.valor.com.br/empresas', 'empresas'],
				['http://www.valor.com.br/agro', 'agronegocio']
				]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("valor.com.br")
		print('---------------------------------------------')

		self.proccess()
		self.commit()
		
		print('---------------------------------------------')


