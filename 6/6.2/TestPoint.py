import unittest
import math

from points import *

class TestFracs(unittest.TestCase):

    def setUp(self):
        self=Point(2,1)

    def test_eq_frac(self):
		print("IS EQUAL - TEST")
		a=Point(2,1)
		b=Point(2,1)
		z=a.__eq__(b)
		self.assertEqual(z,True)
		a=Point(1,1)
		b=Point(2,1)
		z=a.__eq__(b)
		self.assertEqual(z,False)
		a=Point(1,2)
		b=Point(2,1)
		z=a.__eq__(b)
		self.assertEqual(z,False)
		a=Point(2,2)
		b=Point(2,1)
		z=a.__eq__(b)
		self.assertEqual(z,False)
		
    def test_ne_frac(self):
		print("IS NOT EQUAL - TEST")
		a=Point(2,1)
		b=Point(2,1)
		z=a.__ne__(b)
		self.assertEqual(z,False)
		a=Point(1,1)
		b=Point(2,1)
		z=a.__ne__(b)
		self.assertEqual(z,True)
		a=Point(1,2)
		b=Point(2,1)
		z=a.__ne__(b)
		self.assertEqual(z,True)
		a=Point(2,2)
		b=Point(2,1)
		z=a.__ne__(b)
		self.assertEqual(z,True)
		
    def test_add_frac(self):
		print("ADD - TEST")
		a=Point(2,1)
		b=Point(3,1)
		z=a.__add__(b)
		self.assertEqual(z.x,5)
		self.assertEqual(z.y,2)		
		a=Point(-20,13)
		b=Point(5,1)
		z=a.__add__(b)
		self.assertEqual(z.x,-15)
		self.assertEqual(z.y,14)
		
    def test_sub_frac(self):
		print("SUB - TEST")
		a=Point(1,1)
		b=Point(1,2)
		c=Point(20,5)
		d=Point(2,1)
		z=a.__sub__(b)
		self.assertEqual(z.x,0)
		self.assertEqual(z.y,-1)
		z=c.__sub__(d)
		self.assertEqual(z.x,18)
		self.assertEqual(z.y,4)

    def test_mul_frac(self):
		print("MUL - TEST")
		a=Point(1,1)
		b=Point(1,2)
		c=Point(20,5)
		d=Point(2,1)
		z=a.__mul__(b)
		self.assertEqual(z.x,1)
		self.assertEqual(z.y,2)
		z=c.__mul__(d)
		self.assertEqual(z.x,40)
		self.assertEqual(z.y,5)
		
    def test_cross_frac(self):
		print("CROSS - TEST")
		a=Point(2,1)
		b=Point(2,1)
		z=a.__cross__(b)
		self.assertEqual(z,0)
		a=Point(1,1)
		b=Point(2,1)
		z=a.__cross__(b)
		self.assertEqual(z,-1)
		a=Point(1,2)
		b=Point(2,1)
		z=a.__cross__(b)
		self.assertEqual(z,-3)
		a=Point(2,2)
		b=Point(2,1)
		z=a.__cross__(b)
		self.assertEqual(z,-2)	

    def test_lenn_frac(self):
		print("LENGHT - TEST")
		a=Point(2,1)
		z=a.length()
		self.assertEqual(z,math.sqrt(5))

if __name__ == '__main__':
    unittest.main()  
