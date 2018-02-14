import string

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
	'sob', 
	'sobre', 
	'trás',
	'à',
	'aquele',
	'duma',
	'disto',
	'na',
	'nas',
	'num',
	'numa',
	'nuns',
	'numas',
	'nessa',
	'pelo',
	'pelas',
	'a',
	'o',
	'as',
	'os',
	'ao',
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
	'um',
	'no',
	'que'
]

def tagfy(title):
	tagfied = []
	
	title = title.lower()
	title = strip_punctuation(title)
	
	terms = title.split(" ")

	for term in terms:
		if not (term in prep):
			tagfied.append(term)
	
	return tagfied

	
def strip_punctuation(s):
    return ''.join(c for c in s if c not in string.punctuation)


