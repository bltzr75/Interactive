import json
from difflib import SequenceMatcher, get_close_matches
dictionary = json.load(open("dictionary.json")) 

def search_in_dict():
    word = (input("Searching for definition of: ").lower()).strip()
    if word == "" or word.isnumeric():
        return("Please put a word")
    elif word in dictionary:
        return dictionary[word]        
    elif compare(word, dictionary):
        yn= input (("The word doesn't exist. Did you mean %s?. Enter 'Y' or 'N' " % str(compare(word, dictionary)) )).upper()   
        if yn == "Y":
            return dictionary[str(compare(word, dictionary))]
        else:
            return("Ok. Please, try again.")
    elif word not in dictionary:
        return("The word doesn't exist. Please check again.")    
    else: 
        return("No signs allowed in this field.")
    
        
def compare(word, dictionary):
    return get_close_matches(word, dictionary.keys())[0]
        
output= search_in_dict()
count = 1   
for definitions in output:
    print ("Definition Number %d : %s" % ( count,definitions))
    count +=1  

