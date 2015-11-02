ListaI = [-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11]
ListaII = [-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11]

def odwracanieIter(L, left, right):
	while left<right:
		helper = L[left]
		L[left] = L[right]
		L[right] = helper
		left+=1
		right-=1

def odwracanieReku(L, left, right):
	if left<right:
		helper = L[left]
		L[left]=L[right]
		L[right]=helper
		odwracanieReku(L,left+1,right-1)

odwracanieIter(ListaI,1,7)
odwracanieReku(ListaII,1,7)

print (ListaI)
print (ListaII)
