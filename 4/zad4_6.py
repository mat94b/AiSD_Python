seq = [1,[2,[1,1],3],3,[1,2,3]]

def s_s(s,su):
	suma = su
	for e in s:
		if isinstance(e,int):
			suma+=e
		if isinstance(e,(list,tuple)):
			suma+=s_s(e,0)
	return suma

def sum_seq(sequence):
	if isinstance(sequence,(list,tuple)):
		return s_s(sequence,0)		
	else:
		print("TO NIE JEST SEKWENCJA")

print(sum_seq(seq))
