from fractions import gcd

class Fracs:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __str__(self):
		final=""
		if self.y==1:
			final = str(self.x)
			return final
		elif self.y!=1:
			final=str(self.x)+"/"+str(self.y)
			return final

	def __repr__(self):
		return "Fracs("+self.x+","+self.y+")"
		
	def __add__(self,other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		newL = (m2*l1)+(l2*m1)
		newM = m2*m1
		res = Fracs(newL, newM)
		m = gcd(res.x, res.y)
		res.x = res.x / m
		res.y = res.y / m
		return res
		
	def __sub__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		newL = (m2*l1)-(l2*m1)
		newM = m2*m1
		res = Fracs(newL, newM)
		m = gcd(res.x, res.y)
		res.x = res.x / m
		res.y = res.y / m
		return res
		
	def __mul__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		newL = l1*l2
		newM = m2*m1
		res = Fracs(newL, newM)
		m = gcd(res.x, res.y)
		res.x = res.x / m
		res.y = res.y / m
		return res
		
	def __div__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		tmp=m2
		m2=l2
		l2=tmp
		newL = l1*l2
		newM = m2*m1
		res = Fracs(newL, newM)
		m = gcd(res.x, res.y)
		res.x = res.x / m
		res.y = res.y / m
		return res
		
	def __pos__(self):
		m=self.x
		n=self.y
		if (m>0 and n<0) or (m<0 and n>0):
			self.y*=(-1)
			m = gcd(self.x, self.y)
			self.x = self.x / m
			self.y = self.y / m
			return self
		if m<0 and n<0:
			self.y*=(-1)
			self.x*=(-1)
			m = gcd(self.x, self.y)
			self.x = self.x / m
			self.y = self.y / m
			return self
		else:
			return self
			
	def __neg__(self):
		m=self.x
		n=self.y
		if (m>0 and n>0) or (m<0 and n<0):
			self.y*=(-1)
			return self
		else:
			return self
			
	def __invert__(self):
		r = Fracs(self.y, self.x)
		return r

	def __cmp__(self, other):
		l1=float(self.x)
		l2=float(other.x)
		m1=float(self.x)
		m2=float(other.y)
		jeden = float(l1/m1)
		dwa = float(l2/m2)
		if jeden<dwa:
			return -1
		elif dwa<jeden:
			return 1
		else:
			return 0
			
	def __float__(self):
		l=float(self.x)
		return float(l/self.y)
	




