import sys
sys.path.append('../newspaper')

from newspaper import Article
import requests
from bs4 import BeautifulSoup as bs
from tagfy import tagfy
from crawler import crawler
from newslog import crawlerlog
import datetime

class crawlerBovespa(crawler):
	
	def __init__(self):
		crawler.__init__(self)

	def proccess(self):
		for url in self.urls:
			print("Endereço principal -> ", url[0])
			print("")

			crLog = crawlerlog()
			crLog.openFile("log/bovespa/"+url[1]+"log.txt")

			p = requests.get(url[0])
			s = bs(p.content, 'html.parser')

			links = s.find_all('main', {'id':'noticias'})
			links = links[0].find_all('a')
			
			for link in links:
				newsurl = link['href']
				
				title, date, text = parserBovespaNews(url[0]+newsurl[2:])

				print(title)
				print(date)
				print(text)

				if len(title) == 0:
					break
				
				if not crLog.oldNews(title):
					self.save([date, 
								newsurl,
								url[0],
								url[1],
								title,
								text,
								'',
								tagfy(title),
								"bmfbovespa"
							])
			crLog.closeFile()
			
	def run(self):

		urls = [['http://www.bmfbovespa.com.br/pt_br/noticias/', 'economia']]

		self.setUrl(urls)

		print('---------------------------------------------')
		print("bmfbovespa.com.br")
		print('---------------------------------------------')

		self.proccess()
		self.commit()

		print('---------------------------------------------')

def parserBovespaNews(url):
	title = ''
	date = ''
	text = ''
	newdate = None

	p = requests.get(url)
	parser = bs(p.content, 'html.parser')

	article = parser.find_all('article')
	
	if len(article) > 0:
		tagsh2 = article[0].find_all('h2')
		title = tagsh2[0].text

		tagsmall = article[0].find_all('small')
		date = tagsmall[0].text
		date = date.replace("/", "-")
		date += " 00:00:01.500000"
		newdate = datetime.datetime.strptime(date, "%d-%m-%y %H:%M:%S.%f")

		tagp = article[0].find_all('p')
		for p in tagp:
			text += p.text
	
	return title, newdate, text

