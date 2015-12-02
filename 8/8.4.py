def heron(a, b, c):
	try:
		if a<=0 or b<=0 or c<=0:
			raise ValueError
		p=(a+b+c)/2
		return p
	except ValueError: 
		print("BOKI NIE SPELNIAJA WARUNKU TROJKATA")