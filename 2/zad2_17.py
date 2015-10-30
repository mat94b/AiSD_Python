line = "Gammmma Alaaaaafa Delta Tanngo Be"
napis = ""
L = list()
for char in line:
	if char!=' ' and char!='\t' and char!='\n':
		napis =  napis+char
	else:
		L.append(napis)
		napis=""
L.append(napis)
sortedL=sorted(L)
print("Posortowane alfabetycznie:")
print(sortedL)
print("Posortowane wedlug wielkosci:")
sortedLong=sorted(L, key=len , reverse=True) 
print(sortedLong)
