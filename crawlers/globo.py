import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
from tagfy import tagfy
from crawler import crawler
from newslog import crawlerlog

class crawlerGlobo(crawler):
	
	def __init__(self):
		crawler.__init__(self)

	def proccess(self):
		for url in self.urls:
			print("Endereço principal -> ", url[0])
			print("")

			crLog = crawlerlog()
			crLog.openFile("log/globo/"+url[1]+"log.txt")

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			links = s.find_all('a', {'class':'feed-post-link'})

			for link in links:
				newsurl = link['href']
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
										"globo"
									])
			crLog.closeFile()


	def run(self):

		urls = [['http://g1.globo.com/economia/', 'economia'],
										['http://g1.globo.com/economia/negocios/', 'negocios'],
										['http://g1.globo.com/economia/agronegocios/', 'agronegocios'],
										['http://g1.globo.com/politica/', 'politica']
										]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("Globo.com")
		print('---------------------------------------------')

		self.proccess()
		self.commit()

		print('---------------------------------------------')
