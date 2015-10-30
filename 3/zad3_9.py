string = ('[','[','(',2,'1',')',']','(',2,1,2,')','[',2,1,2,3,']',']')
counter=0
final="["
controler=0

for x in string:
	if x=='[' or x=='(' or x=='{':
		controler+=1
	if isinstance(x,int):
		counter+=x
	if x==']' or x==')' or x=='}':
		controler-=1
		if controler>0:
			final=final+str(counter)+", "
			counter=0
omega = final[:-2]
omega=omega+"]"
print(omega)