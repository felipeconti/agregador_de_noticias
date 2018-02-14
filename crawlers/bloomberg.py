import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re

def crawlerUol():
	urls = ['https://www.bloomberg.com.br/blog/'
			]

	print('---------------------------------------------')
	print("bloomberg.com.br")
	print('---------------------------------------------')

	for url in urls:
		print("Endereço principal -> ", url)
		print("")

		p = requests.get(url)
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

		print('---------------------------------------------')
		
crawlerUol()