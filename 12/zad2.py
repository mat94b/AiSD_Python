# v.2.0

def binarne_rek(L, left, right, y):
	if right < left:
		return False
	zm = (left+right)/2
	if L[zm] is y:
		return zm
	elif L[zm] < y:
		return binarne_rek(L, zm + 1, right, y)
	else:
		return binarne_rek(L, left, zm, y)
