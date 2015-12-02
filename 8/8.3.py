import random

def calc_pi(n):
	a = 100 				# dlugosc boku kwadratu
	r = float(a/2)
	aimed = 0
	for x in range(0,n,1):
		x = random.randrange(0,a)
		y = random.randrange(0,a)
		controler = False
		if ((x-r)*(x-r))+((y-r)*(y-r))<=(r*r):
			aimed += 1
	aimed*=4
	pi = float(float(aimed))/float(n)
	print(str(pi))
	return pi
	
calc_pi(100)	
calc_pi(1000)
calc_pi(10000)	
calc_pi(100000)
calc_pi(1000000)	
calc_pi(10000000)