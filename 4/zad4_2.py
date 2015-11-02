# <!--- ZADANIE 1 --->
leng = 13 #dlugosc miarki
# <!--- ZADANIE 2 --->
szerokosc = 4 # ilosc kratek na szerokosc
wysokosc = 2 # ilosc kratek na wysokosc
def funkcja35(dl):
	fline="|"
	sline=""
	co=0
	h=0
	for x in range(0,leng,1):
		fline=fline+"----|"
	final=fline+"\n"
	for x in final:
		if x=='|':
			if h>=10:
				sline = sline[:-1]
			sline+=str(h)
			h+=1
		else:
			sline+=' '

	omega=fline+"\n"+sline
	print(omega)
def funkcja36(s, w):
	a=""
	for x in range(0,w,1):
		for y in range(0,s,1):
				a=a+"+---"
		a=a+"+\n"
		for y in range(0,s+1,1):
				a=a+"|   "
		a=a+"\n"
	for y in range(0,s,1):
		a=a+"+---"
	a=a+"+"
	print (a)
					
funkcja35(leng)
funkcja36(szerokosc, wysokosc)
