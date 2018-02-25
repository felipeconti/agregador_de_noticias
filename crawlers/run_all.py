import sys
from globo import crawlerGlobo
from uol import crawlerUol
from bloomberg import crawlerBloomberg
from valoreconomico import crawlerValorEconomico


crGlobo = crawlerGlobo()
crGlobo.run()

crUol = crawlerUol()
crUol.run()

crBloomberg = crawlerBloomberg()
crBloomberg.run()

crValor = crawlerValorEconomico()
crValor.run()

