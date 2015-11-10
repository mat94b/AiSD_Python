from fractions import gcd

def shortest(frac):
    m = gcd(frac[0], frac[1])
    frac[0] = frac[0] / m
    frac[1] = frac[1] / m
    return frac

def add_frac(f1, f2):
	l1=f1[0]
	l2=f2[0]
	m1=f1[1]
	m2=f2[1]
	newL = (m2*l1)+(l2*m1)
	newM = m2*m1
	newF = [newL, newM]
	return shortest(newF)
	
def sub_frac(f1, f2):
	l1=f1[0]
	l2=f2[0]
	m1=f1[1]
	m2=f2[1]
	newL = (m2*l1)-(l2*m1)
	newM = m2*m1
	newF = [newL, newM]
	return shortest(newF)
	
def mul_frac(f1, f2):
	l1=f1[0]
	l2=f2[0]
	m1=f1[1]
	m2=f2[1]
	newL = l1*l2
	newM = m2*m1
	newF = [newL, newM]
	return shortest(newF)
	
def div_frac(f1, f2):
	l1=f1[0]
	l2=f2[0]
	m1=f1[1]
	m2=f2[1]
	tmp=m2
	m2=l2
	l2=tmp
	newL = l1*l2
	newM = m2*m1
	newF = [newL, newM]
	return shortest(newF)
	
def is_positive(frac):
	l=frac[0]
	m=frac[1]
	if l==0:
		return null
	if l<0 and m>0:
		return False
	if l>0 and m<0:
		return False
	if (l<0 and m<0) or (l>0 and m>0):
		return True
		
def is_zero(frac):
	l=frac[0]
	if l==0:
		return True
	else:
		return False
		
def cmp_frac(f1,f2):
	l1=float(f1[0])
	l2=float(f2[0])
	m1=float(f1[1])
	m2=float(f2[1])
	jeden = float(l1/m1)
	dwa = float(l2/m2)
	if jeden<dwa:
		return -1
	elif dwa<jeden:
		return 1
	else:
		return 0
		
def frac2float(frac):
	l=float(frac[0])
	m=float(frac[1])
	flt=float(l/m)
	return flt