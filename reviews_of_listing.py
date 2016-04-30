from py2neo import Graph
from langdetect import detect
import nltk.data
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer

tknzr = TweetTokenizer()
lmtzr = WordNetLemmatizer()
graph = Graph("http://neo4j:nA>R67;od0ex82X6(<x9C]1|f4SYuM:l@10.8.0.1:7474/db/data")
assert graph.neo4j_version == (2, 3, 2)

#Run the query which gets all the reviews of the listing with the given ID and print them all

k = graph.cypher.execute("MATCH (l:Listing {listing_id:38179})-[rel:HAS_REVIEW]->(r:Review) RETURN r.comments AS COMMENT")
print k

#Split the reviews and get them one by one for pre-processing
review1=k[16]
print review1

#Convert the text review to string and run a language detector 
mystring = str(review1)
answer = detect(mystring)

if answer=='en':
	print answer
	sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	sentences = sentence_detector.tokenize(mystring.strip())
	print "Lemmatized -->"
	for item in sentences: 
		mysentencetokens = tknzr.tokenize(item)
	
	#Lemmatize the tokenized sentences
		looper = 0
		for token in mysentencetokens:
			mysentencetokens[looper] = lmtzr.lemmatize(token)
			looper += 1
		print mysentencetokens
	
	
	
else: #should not print something just to go on to the other review. thats just a momentan setting
	print "Language is not english. Sorry, this review cannot be processed."
