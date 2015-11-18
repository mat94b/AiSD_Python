import unittest

from fracs import *

class TestFracs(unittest.TestCase):

    def setUp(self):
        self=Fracs(2,1)

    def test_add_frac(self):
		print("ADD - TEST")
		a=Fracs(2,1)
		b=Fracs(3,1)
		z=a.__add__(b)
		self.assertEqual(z.x,5)
		self.assertEqual(z.y,1)
		
    def test_sub_frac(self):
		print("SUB - TEST")
		a=Fracs(1,1)
		b=Fracs(1,2)
		c=Fracs(20,5)
		d=Fracs(2,1)
		z=a.__sub__(b)
		self.assertEqual(z.x,1)
		self.assertEqual(z.y,2)
		z=c.__sub__(d)
		self.assertEqual(z.x,2)
		self.assertEqual(z.y,1)
		
    def test_mul_frac(self):
		print("MUL - TEST")
		a=Fracs(1,2)
		b=Fracs(2,1)
		c=Fracs(20,5)
		d=Fracs(2,1)
		z=a.__mul__(b)
		self.assertEqual(z.x,1)
		self.assertEqual(z.y,1)
		z=c.__mul__(d)
		self.assertEqual(z.x,8)
		self.assertEqual(z.y,1)	

    def test_div_frac(self):
		print("DIV - TEST")
		a=Fracs(8,2)
		b=Fracs(2,1)
		c=Fracs(20,5)
		d=Fracs(2,1)
		z=a.__div__(b)
		self.assertEqual(z.x,2)
		self.assertEqual(z.y,1)
		z=c.__div__(d)
		self.assertEqual(z.x,2)
		self.assertEqual(z.y,1)		

    def test_pos_frac(self):
		print("POS - TEST")
		a=Fracs(1,2)
		b=Fracs(-1,-2)
		c=Fracs(-20,5)
		d=Fracs(100,-1)
		z=a.__pos__()
		self.assertEqual(z.x,1)
		self.assertEqual(z.y,2)
		z=b.__pos__()
		self.assertEqual(z.x,1)
		self.assertEqual(z.y,2)
		z=c.__pos__()
		self.assertEqual(z.x,4)
		self.assertEqual(z.y,1)
		z=d.__pos__()
		self.assertEqual(z.x,100)
		self.assertEqual(z.y,1)
		
    def test_pos_frac(self):
		print("NEG - TEST")
		a=Fracs(1,2)
		b=Fracs(-1,-2)
		c=Fracs(-20,5)
		d=Fracs(100,-1)
		z=a.__neg__()
		self.assertEqual(z.x,1)
		self.assertEqual(z.y,-2)
		z=b.__neg__()
		self.assertEqual(z.x,-1)
		self.assertEqual(z.y,2)
		z=c.__neg__()
		self.assertEqual(z.x,-20)
		self.assertEqual(z.y,5)
		z=d.__neg__()
		self.assertEqual(z.x,100)
		self.assertEqual(z.y,-1)	

    def test_inv_frac(self):
		print("INV - TEST")
		a=Fracs(1,2)
		z=a.__invert__()
		self.assertEqual(z.x,2)
		self.assertEqual(z.y,1)
		
    def test_cmp_frac(self):
		print("CMP - TEST")
		b=Fracs(1,1)
		c=Fracs(1,1)
		d=Fracs(4,1)
		z=c.__cmp__(d)
		self.assertEqual(z,-1)
		z=b.__cmp__(c)
		self.assertEqual(z,0)

if __name__ == '__main__':
    unittest.main()  