# -*- coding: utf-8 -*-
# Problem ośmiu HetmanProblemów.
# Wiersze i kolumny mają zakres od 0 do N-1.

def rysuj():
    for w in range(N):
        wiersz = ""
        for k in range(N):
            if x[k] == w:
                wiersz += "H  "
            else:
                wiersz += ".  "
        print(wiersz)


def dopuszczalny(w, k):
    global hel
    wynik = a[w] and b[w + k] and c[w - k]
    if wynik == False:
        return False
    else:
        pom = list(x)
        pom[k] = w
        if None in pom:
            return True
        else:  # sprawdzenie czy juz nie bylo takiego rozwiazanie
            if pom in hel:
                return False
            else:
                hel.append(pom)
                return True


def zapisz(w, k):
    x[k] = w
    a[w] = False
    b[w + k] = False
    c[w - k] = False


def wymaz(w, k):
    a[w] = True
    b[w + k] = True
    c[w - k] = True


def probuj(k):
    udany = False
    w = 0  # numery od 0 do N-1
    while (not udany) and (w < N):
        if dopuszczalny(w, k):
            zapisz(w, k)
            if k < (N - 1):
                udany = probuj(k + 1)
                if not udany:
                    wymaz(w, k)
            else:
                udany = True
        w = w + 1
    return udany

def HetmanProblem(rozmiar):
    if rozmiar < 1:
        raise ValueError
    global N
    global a
    global b
    global c
    global x
    global hel

    N = rozmiar 
    x = N * [None]
    a = N * [True]
    b = (2 * N - 1) * [True]
    c = (2 * N - 1) * [True]
    hel = []
    rozw = 0
    if rozmiar ==1:
        print "Plansza 1x1:\nH\n"
    if rozmiar ==2:
        print "Plansza 2x2:\n . H\nH .\n\noraz\n H .\n. H\n"
    if rozmiar ==3:
        print "Plansza 3x3:\n . . H\n. H .\nH . .\n\noraz\n H . .\n. H .\n. . H\n"
    else:
        while(1):
            a = N * [True]
            x = N * [None]
            b = (2 * N - 1) * [True]
            c = (2 * N - 1) * [True]
            if(probuj(0)):
                rozw +=1
                print
                print "Plansza: " + str(N)
                print"Rozwiązanie " + str(rozw)
                rysuj()
            else: break

        if rozw ==0:
            print "Rozmiar planszy: " + str(N)
            print "Brak rozwiazan"

for i in range(2,6):
    HetmanProblem(i)
