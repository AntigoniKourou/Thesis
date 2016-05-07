from py2neo import Graph
import nltk.data
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment 
import time
import csv
from language_check import language_checker
from lemmatization import lemmatizer
from feature_identification import identifier


#start tracking the execution time
start_time = time.time()



graph = Graph("http://neo4j:nA>R67;od0ex82X6(<x9C]1|f4SYuM:l@10.8.0.1:7474/db/data")
assert graph.neo4j_version == (2, 3, 2)

#Run the query which gets all the reviews of the listing with the given ID and print them all
all_listings=open('listings.csv','rb')
spamreader = csv.reader(all_listings, delimiter=' ', quotechar='|')
b=0

for row in spamreader:
	if b<2:
		true=True
		query1= "MATCH (l:Listing {listing_id:"
		query2="})-[rel:HAS_REVIEW]->(r:Review) RETURN r.comments AS COMMENTS"
		myrow=str(row).replace('[','').replace('\'','').replace(']','')
		query = query1 + str(myrow) + query2
		k = graph.cypher.execute(query)
		print k
		b=b+1

		
# Convert the text review to string and run a language detector. If the langage is english
# the script will slipt the sentences and will send each of them to the sentiment detector.	

		for review in k:
			mystring = str(review).replace('-','').replace('COMMENTS','')
			check = language_checker(mystring)
			if (check=='en'):	
				sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
				sentences = sentence_detector.tokenize(mystring.strip())
				
#Vader sentiment detection - detects the sentiment for each sentence
				for sentence in sentences:
					print sentence
					vs = vaderSentiment(sentence)
# Lemmatize each word in the text  to bring to the basic form
					lemmatized = lemmatizer(sentence)
					print lemmatized
					print "\n\t" + str(vs)
					probabilities = identifier(sentence)
	
				

print("--- %s seconds ---" % (time.time() - start_time))