word="motor"
finalResult=""
for char in word:
	finalResult=finalResult+char
	finalResult=finalResult+"_"
b=finalResult[:-1]
print("Slowo na wejsciu: %s"%word)
print ("Slowo na wyjsciu: %s"%b)
