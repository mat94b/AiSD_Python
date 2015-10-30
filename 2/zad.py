line ="12\n3\t"
counter = 0
for char in line:
	if char!=' ' and char!='\t' and char!='\n':
		counter+=1
print(counter)
