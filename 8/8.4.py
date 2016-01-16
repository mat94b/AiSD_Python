# v.2.0
import math

def heron(a, b, c):
	try:
		if (a+b<=c) or (a+c<=b) or (b+c<=a):
			raise ValueError
		a = float(a); b = float(b); c = float(c)
		p = float((a+b+c)/2)
		S = math.sqrt(p*(p-a)*(p-b)*(p-c))
		return S
	except ValueError: 
		print("BOKI NIE SPELNIAJA WARUNKU TROJKATA")
