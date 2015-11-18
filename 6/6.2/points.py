import math

class Point:
	def __init__(self, x=0, y=0):  
		self.x = x
		self.y = y
		
	def __str__(self):
		return ("("+str(self.x)+","+str(self.y)+")")
		
	def __repr__(self):
		return "Point("+self.x+","+self.y+")"
	
	def __eq__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		if l1==l2 and m1==m2:
			return True
		else:
			return False
			
	def __ne__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		if (l1!=l2 or m1!=m2):
			return True
		else:
			return False
			
	def __add__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		nl=l1+l2
		nm=m1+m2
		return Point(nl,nm)
		
	def __sub__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		nl=l1-l2
		nm=m1-m2
		return Point(nl,nm)

	def __mul__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		nl=l1*l2
		nm=m1*m2
		return Point(nl,nm)
		
	def __cross__(self, other):
		l1=self.x
		l2=other.x
		m1=self.y
		m2=other.y
		res=l1*m2-m1*l2
		return res
		
	def length(self):
		a=self.x
		b=self.y
		a*=a
		b*=b
		res = math.sqrt(a+b)
		return res
