
def identifier(sentence)

#features = ['accuracy','check-in','cleanliness','communication','location','value']
features=['internet']

# We have six features for the moment. The list can of course be extended.
# In a sentence we can identifi noone or all of these features.
# The sentiment score of each sentence would have a probability 1/6 chances that it would refer
# to one of these features if they are all mentioned.
# if only one feature is mentioned, then the sentiment score would be 100% (or 1) for this certain feature
# that we found to be mentioned. Clearly the sum of probabilities for each sentence
# every time, shall be 1. 
item=0
count = 0
found = False
output =[0,0,0,0,0,0]
#the output shall be something like: (0,1,0,0,1,0) where 0 means the feature is not mentioned and 1 the opposite 
try:
	while item < len(features):
		synonyms = open(item + ".txt", "r")
		lines = synonyms.readlines()
		for line in lines:
			for word in sentence:
				if line==word:
					found=True
		if found == True:
			output[item]=1
			count +=1
			item +=1		
	for element in output:
		element=element/count
	return output
except:
	return output