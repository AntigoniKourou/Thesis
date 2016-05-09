#Remove all the duplicates from the list of synonmys 						
newlist = []
features = ['accuracy','check-in','cleanliness','communication','location','value']
for feature in features:
	f = open('C:/Python27/ontology/'+ feature + '_noduplicates.txt','w')
	text_file = open('C:/Python27/ontology/'+ feature + '.txt', 'r')
	lines = text_file.readlines()
	for line in lines:
		if line not in newlist:
			newlist.append(line)
	
	for  item in newlist:
		f.write(item)