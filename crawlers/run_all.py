import sys
from globo import crawlerGlobo
from uol import crawlerUol
from bloomberg import crawlerBloomberg
from valoreconomico import crawlerValorEconomico
from postgres import postgres

db = postgres()
db.connect()

crGlobo = crawlerGlobo()
crGlobo.run(db)

crUol = crawlerUol()
crUol.run(db)

crBloomberg = crawlerBloomberg()
crBloomberg.run(db)

crValor = crawlerValorEconomico()
crValor.run(db)


db.closeconn()