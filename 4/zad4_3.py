def factorial(n):
	xyz = 1
	while n>=1:
		xyz=xyz*n
		n=n-1
	return xyz
for z in range(15):
	print(factorial(z))
