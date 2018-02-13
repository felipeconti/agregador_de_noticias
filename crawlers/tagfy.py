
prep = ['a', 
	'ante', 
	'após', 
	'até', 
	'com', 
	'contra', 
	'de', 
	'desde', 
	'em', 
	'entre', 
	'para', 
	'por', 
	'perante', 
	'sem', 
	'sob', 
	'sobre', 
	'trás',
	'à',
	'aquele',
	'duma',
	'disto',
	'nas',
	'num',
	'nessa',
	'pelo',
	'pelas',
	'a',
	'o',
	'as',
	'os',
	'do',
	'da',
	'dos',
	'das',
	',',
	'.',
	'"',
	"'",
	'(',
	')',
	'é',
	'e',
	'um'
]

def tagfy(title):
	terms = title.split(" ")
	cmp(prep, terms)

	#TODO: Terminar o tagfy!!!!!!

tagfy("esse é um texto de teste")
