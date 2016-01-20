def selection_sort(L):
    for step in range(len(L)):
        location_of_smallest = step
        for location in range(step, len(L)):
            if L[location] < L[location_of_smallest]:
                location_of_smallest = location
        temporary_item = L[step]
        L[step] = L[location_of_smallest]
        L[location_of_smallest] = temporary_item

def mediana(L,left,right):    
	selection_sort(L)
	print L
	if len(L)%2 is 1:
		return L[(len(L)+1)/2]
	else:
		return (L[(len(L))/2] + L[((len(L))/2)+1]) / 2
