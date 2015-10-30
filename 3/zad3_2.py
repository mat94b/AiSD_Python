L=[3,1,2]
L = L.sort()
x, y,z = 1, 2, 3
X = [1, 2, 3 ]; X[1] = 4
X = [1, 2, 3] ; X[2] = 4
X = "abc" ; X="abcd"
def pow(T):
    return ((float(9)/5)*T + 32)
map(pow, range(8))


# <---------------  I PROBLEM  --------------->
# nie ma zadeklarowanej zmiennej.
# chcemy posortowac obiekt, ktory nie jest nigdzie zadeklarowany,
# nie wiadomo czym jest L, 
# prosty sposob naprawy to dopisanie L=[3,1,2] przed L=L.sort()

# <---------------  II PROBLEM  --------------->
# kolejnym problemem jest to ze probujemy wpisac trzy wartosci w dwie zmienne,
# aby naprawic problem wystarczy wpisac x,y,z=1,2,3


# <---------------  III,IV PROBLEM  --------------->
# kolejno w X =1,2,3 brakowalo nawiasow
# natomiast w X=[1,2,3] nawiasy byly, ale X[3] <- odwoluje sie do nieistniejacej
# komorki w tabeli, i napotyka na blad, poniewaz komorki sa numerowane od 0,
# ostatnia ma index 2 X[2]=4 (tak to powinno wygladac)

# <---------------  V PROBLEM  --------------->
# kolejnym problemem jest to, ze X="abc" nie jest lista tylko String'iem
# a .append dodaje wyraz na koniec listy, przykladowe rozwiazanie: X="abcd"

# <---------------  VI PROBLEM  --------------->
# map przyjmuje 2 argumenty a dostalo 1, poniewaz funkcja pow nie zostala 
# wczesniej zadeklarowana, pozwolilem sobie zadeklarowac jakas funkcje,

# <---------------  VII PROBLEM  --------------->
# wprowadzilem przykladowe zmiany w kodzie aby sie kompilowal
