checker = True
n=0
while(checker):
	print("///// aby zakonczyc wpisz 'stop'")
	try:
		n=raw_input('Podaj liczbe: ')		
		if n=="stop":
			exit()
		n=int(n)
		if isinstance( n, int ):
			pow3 = n*(n*n)
			print("Liczba:"); print(n)
			print("Trzecia potega:");print(pow3)

	except Exception:
		print("Zle wprowadzono dane, podaj liczbe lub komende 'stop'")