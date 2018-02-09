import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs

def crawlerGlobo():
	urls = ['http://g1.globo.com/economia/',
			'http://g1.globo.com/economia/negocios/',
			'http://g1.globo.com/economia/agronegocios/',
			'http://g1.globo.com/politica/'
			]

	print('---------------------------------------------')
	print("Globo.com")
	print('---------------------------------------------')

	for url in urls:
		print("Endereço principal -> ", url)
		print("")

		p = requests.get(url)
		s = bs(p.content, 'html.parser')

		links = s.find_all('a', {'class':'feed-post-link'})

		for link in links:
			newsurl = link['href']
			article = Article(newsurl)
			article.download()
			article.parse()
			print("Data de publicacao: ", article.publish_date)
			#print("Autores: ", article.authors)
			print("Titulo: ", article.title)
			print("Link: ", newsurl)
			print("")
			#article.text

		print('---------------------------------------------')