import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
import re
from tagfy import tagfy
from crawler import crawler
from newslog import crawlerlog
from datetime import datetime

class crawlerInfomoney(crawler):

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

			newslist = s.find_all('a', {'class':'title-box title-box-medium' })

			for singlenews in newslist:
				newsurl = singlenews['href']
				article = Article('http://www.infomoney.com.br'+newsurl)
				article.download()
				article.parse()

				#Como não conseguia fazer o parser de data, faço na mão
				date = s.find_all('input', {'id':'generatedAt'})
				date = date[0]['value'].replace('/','-')
				date = date+'+00:00'
				datefinal = date[6:10]+'-'+date[3:5]+'-'+date[:2]+' 00:00:00.000'

				print(datetime.strptime(datefinal, '%Y-%m-%d %H:%M:%S.%f'))

				print("Data de publicacao: ", date)
				print("Titulo: ", article.title)
				print("Link: ", newsurl)
				print("")
				
				if not crLog.oldNews(article.title):
					self.save([datetime.strptime(datefinal, '%Y-%m-%d %H:%M:%S.%f'), 
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


	


	

