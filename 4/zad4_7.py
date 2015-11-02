seq = [1,[2,[1,1],3],3,[1,2,3],2]

def s_s(s,su):
	suma = su
	for e in s:
		if isinstance(e,int):
			suma+=1
		if isinstance(e,(list,tuple)):
			suma+=s_s(e,0)
	return suma

def flatten(sequence):
	if isinstance(sequence,(list,tuple)):
		return s_s(sequence,0)		
	else:
		print("TO NIE JEST SEKWENCJA")

print(flatten(seq))
