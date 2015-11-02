def fibonacci(n):
	x=1
	y=1
	temp=0
	if n==1 or n==2:
		return 1
	if n==0:
		return 0
	else:
		for i in range(0,n-1,1):
			temp=y
			y+=x
			x=temp
		return y

for z in range (0,15,1):
	print(fibonacci(z))
