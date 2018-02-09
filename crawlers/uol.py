import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re

def crawlerUol():
	urls = ['https://economia.uol.com.br/noticias/afp/',
			'https://economia.uol.com.br/noticias/ansa/',
			'https://economia.uol.com.br/noticias/bbc/',
			'https://economia.uol.com.br/noticias/bloomberg/',
			'https://economia.uol.com.br/noticias/estadao-conteudo/',
			'https://economia.uol.com.br/noticias/EFE/',
			'https://economia.uol.com.br/noticias/reuters/',
			'https://economia.uol.com.br/noticias/valor-online/'
			]

	print('---------------------------------------------')
	print("uol.com.br")
	print('---------------------------------------------')

	for url in urls:
		print("Endereço principal -> ", url)
		print("")

		p = requests.get(url)
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
			
		print('---------------------------------------------')