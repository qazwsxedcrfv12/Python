                         #Spelling checker in python

from textblob import TextBlob
myList = ["Incorret", "Spellin"]
corrected_list = []
for word in myList:
  corrected_list.append(TextBlob(word))
print("Corrected list words are:")
 
for word in corrected_list:
    print(word.correct(),end=" ")
print(" ")
  
