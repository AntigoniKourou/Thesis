from py2neo import Graph
import csv

graph = Graph("http://neo4j:nA>R67;od0ex82X6(<x9C]1|f4SYuM:l@10.8.0.1:7474/db/data")

#Make sure we've connected properly
assert graph.neo4j_version == (2, 3, 2)

k = graph.cypher.execute("MATCH (n:Country {name: 'Netherlands'})<-[:IN_COUNTRY]-(l:Listing) RETURN l.listing_id AS LISTING_ID_NL")

with open('listings_NL.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for item in k:
	spamwriter.writerow(item)