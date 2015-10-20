line = "Ala ma kota."
napis = ""
L = list()
for char in line:
	if char!=' ' and char!='\t' and char!='\n':
		napis =  napis+char
	else:
		L.append(napis)
		napis=""
L.append(napis)
napis = ""
amo = 0
for x in range(0,len(L),1):
	if len(L[x])>amo:
		amo = len(L)
		napis = L[x]

print("Zdanie: %s"%line)
print("Najdluzszy wyraz: %s"%napis)
print("Dlugosc: %d"%amo)