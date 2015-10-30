line ="12\t3"
counter=0
for char in line:
	if char!=' ' and char!='\t' and char!='\n':
		counter+=1
print("Laczna dlugosc wyrazow to: %d"%counter)
