def factorial( n ):
	if n <1:  
		return 1
	else:
		returnNumber = n * factorial( n - 1 )
		return returnNumber
			
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	   