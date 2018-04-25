import sys
from globo import crawlerGlobo
from uol import crawlerUol
from bloomberg import crawlerBloomberg
from valoreconomico import crawlerValorEconomico
from bovespa import crawlerBovespa
from reuters import crawlerReuters
from infomoney import crawlerInfomoney

crGlobo = crawlerGlobo()
crGlobo.run()

crUol = crawlerUol()
crUol.run()

crBloomberg = crawlerBloomberg()
crBloomberg.run()

crValor = crawlerValorEconomico()
crValor.run()

crValor = crawlerBovespa()
crValor.run()

crReuters = crawlerReuters()
crReuters.run()

crInfomoney = crawlerInfomoney()
crInfomoney.run()