szerokosc = 4 # ilosc kratek na szerokosc
wysokosc = 2 # ilosc kratek na wysokosc

a=""

for x in range(0,wysokosc,1):
	for y in range(0,szerokosc,1):
			a=a+"+---"
	a=a+"+\n"
	for y in range(0,szerokosc+1,1):
			a=a+"|   "
	a=a+"\n"
for y in range(0,szerokosc,1):
	a=a+"+---"
a=a+"+"
print (a)