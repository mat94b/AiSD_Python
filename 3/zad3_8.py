sekwencja1 = "aabcd123"
sekwencja2 = "a2fd34"
L=list()
final1=""
final2=""
# podpunkt a)
for x in sekwencja1:
	con=False
	for o in range(0,len(L),1):
		if x==L[o]:
			con=True
	if con==False:
		L.append(x)
		final2=final2+x
for y in sekwencja2:
	controler = False
	for z in range(0, len(L),1):
		if y==L[z]:
			controler=True
			final1=final1+y
print("Lista powtarzajacych sie znakow:")
print(final1)
# podpunkt b)
print("Lista wszystkich znakow:")
for t in sekwencja2:
	c=False
	for j in range(0,len(L), 1):
		if t==L[j]:
			c=True
		
	if c==False:
		final2+=t

print(final2)