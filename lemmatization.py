from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer

tknzr = TweetTokenizer()
lmtzr = WordNetLemmatizer()

def lemmatizer(item):
	try: 
# Get the tokens of each sentence
		mysentencetokens = tknzr.tokenize(item)
		
# Lemmatize the tokenized sentences
		looper = 0
		for token in mysentencetokens:
			mysentencetokens[looper] = lmtzr.lemmatize(token)
			mysentencetokens[looper] = str(token).replace('[','').replace('u\'','').replace(']','').replace('\'','')
			looper += 1
		return mysentencetokens
	except:
		return "AN ERROR OCCURRED DURING LEMMATIZATION"