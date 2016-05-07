from langdetect import detect

# This method detects the language of a text review and returns if the language is english or not. 
# If the language is english the answer will be EN
# Because cases with more than one language within the text are found, the methods handles the exceptions 
# by categorizing as not english all the cases where errors on defining  text as english are found. 


text=""
def language_checker(text):
	try:
		answer = detect(text)
		return answer
	except: 
		return "notEN"