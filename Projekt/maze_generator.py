from random import shuffle
from random import randrange


def decoreStart():
	print("+---------------------------------------------+")
	print("|                                             |")
	print("|         PROJEKT ZALICZENIOWY                |")
	print("|         GENERATOR LABIRYNTU                 |")
	print("|                                             |")
	print("|     WPISZ WYMIARY                           |")


def make_maze(w, h, o):
	vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
	ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
	hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
	def walk(x, y):
		vis[y][x] = 1
		d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		shuffle(d)
		for (xx, yy) in d:
			if vis[yy][xx]: continue
			if xx == x: hor[max(y, yy)][x] = "+  "
			if yy == y: ver[y][max(x, xx)] = "   "
			walk(xx, yy)
	walk(randrange(w), randrange(h))
	if(o is True):
		for (a, b) in zip(hor, ver):
			print(''.join(a + ['\n'] + b))
	elif(o is False):
		name = raw_input("|     Nazwa pliku: ")
		if (name is ""):
			name = "labirynt"
		plik = open(name, 'w')
		for (a, b) in zip(hor, ver):
			plik.write(''.join(a + ['\n'] + b))
			plik.write('\n')
		plik.close()

def kwadratowe():
	make_maze(2, 2, True)
	make_maze(3, 3, True)
	make_maze(4, 4, True)
	make_maze(5, 5, True)
	make_maze(6, 6, True)
	make_maze(7, 7, True)
	make_maze(8, 8, True)
	make_maze(9, 9, True)


decoreStart()
controler = True
while(controler):
	szerokosc = raw_input("|     Wpisz szerokosc: ")
	wysokosc = raw_input("|     Wpisz wysokosc: ")
	print("|                                             |")
	print("|     WPROWADZONE WYMIARY: "+str(szerokosc)+"x"+str(wysokosc)+"               |")
	print("|                                             |")
	print("|                                             |")
	print("|  S - aby zapisac do pliku                   |")
	print("|  D - aby wyswietlic na ekran                |")
	print("|  K - wygeneruj kilka labiryntow kwadratowych|")
	print("|  E - aby zakonczyc                       |")
	print("|                                             |")
	oper = raw_input("|     Wpisz litere: ")
	if (oper is "D" or oper is "d"):
		print("|                                             |")
		print("|     LABIRYNT:                               |")
		make_maze(int(szerokosc), int(wysokosc), True)
	elif (oper is "S" or oper is "s"):
		print("|                                             |")
		make_maze(int(szerokosc), int(wysokosc), False)
		print("|     ZAPISANO DO PLIKU:                      |")
	elif (oper is "K" or oper is "k"):
		kwadratowe()
	elif (oper is "E" or oper is "e"):
		exit()
