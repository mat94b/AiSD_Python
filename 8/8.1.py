# v.2.0
import math

def solve1(a, b, c):
	if (a==None or a==0) and b!=None and c!=None:
		b = float(b); c = float(c)
		res = float((-c)/b)
		print(str(res))
	if a==None or b==None or c==None or a==0:
		return None
	delta=b*b-(4*a*c)
	if delta<0: 
		print("BRAK MIEJSC ZEROWYCH")
	elif delta==0:
		print("ISTNIEJE JEDNO MIEJSCE ZEROWE: "+str((b*(-1))/(2*a)))
	elif delta>0:
		delta=math.sqrt(delta)
		x=((b*(-1))-delta)/(2*a)
		y=((b*(-1))+delta)/(2*a)
		print("DWA ROZWIAZANIA: "+str(x)+", "+str(y))
