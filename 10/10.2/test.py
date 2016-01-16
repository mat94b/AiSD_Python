import unittest
from zad import *

class Test(unittest.TestCase):
	def setUp(self):
		self.size = 15
        	self.stack = Stack(self.size)
	
	def testemptyTest(self):
		self.assertTrue(self.stack.is_empty())
		self.stack.push(2)
		self.assertFalse(self.stack.is_empty())
		
	def testfullTest(self):
		self.assertFalse(self.stack.is_full())
		for x in range(0,self.size,1):
			self.stack.push(x+10)
		self.assertTrue(self.stack.is_full())
			
	def testpushTest(self):
		for x in range(0,self.size-1,1):
			self.stack.push(x+10)
		self.stack.push(10)
		self.assertRaises(IndexError, lambda: self.stack.push(100))
	
	def testpopTest(self):
		for x in range(0,self.size,1):
			self.stack.push(x+20)
        	for x in range(self.size):
			self.stack.pop()	
        	self.assertRaises(IndexError, lambda: self.stack.pop())	

	def testcomboTest(self):
		self.assertTrue(self.stack.is_empty())
		self.stack.push(2)
		self.assertFalse(self.stack.is_empty())
		self.stack.pop()
		for x in range(0,self.size,1):
			self.stack.push(x+20)	
		self.assertTrue(self.stack.is_full())	
		self.stack.pop()
		self.assertFalse(self.stack.is_full())	
		self.stack.push(2)
		self.assertRaises(IndexError, lambda: self.stack.push(100))
        	for x in range(self.size):
			self.stack.pop()
		self.assertTrue(self.stack.is_empty())
        	self.assertRaises(IndexError, lambda: self.stack.pop())

if __name__ == '__main__':
	unittest.main()  # uruchamia wszystkie testy
