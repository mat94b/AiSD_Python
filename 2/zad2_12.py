line = "Ala ma kota"
buffer = ""
controler = False
controler2 = True
front = ""
back = ""
addOne = ""
for char in line:
	addOne=char
	if controler == False:
		controler = True
		front = front+char
	if char == ' ' or char=='\t' or char=='\n':
		controler=False
		back = back+buffer
	buffer = char
back = back+addOne
print ("Wyraz zlozony z poczatkowych liter: %s"%front)
print ("Wyraz zlozony z koncowych liter: %s"%back)