arr = [[0 for x in range(1000)] for x in range(1000)] 
	
def PR(m,n):
	try: 
		if m<0 or n<0:
			raise ValueError
		elif m==0 and n==0:
			return 0.5
		elif m>0 and n==0:
			return 0.0
		elif m==0 and n>0:
			return 1.0
		if arr[m][n] == 0:
			r = 0.5 * (PR(m-1, n) + PR(m, n-1))
			arr[m][n] = r
			return r
		else:
			return arr[m][n]
	except ValueError:
		return None
		
		
def PI(m,n):
	try: 
		if m<0 or n<0:
			raise ValueError
		elif m==0 and n==0:
			return 0.5
		elif m>0 and n==0:
			return 0.0
		elif m==0 and n>0:
			return 1.0
		return 0.5 * (PI(m-1, n) + PI(m, n-1))
	except ValueError:
		return None
		
