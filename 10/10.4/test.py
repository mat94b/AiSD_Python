import unittest
from zad import *

class TestQueue(unittest.TestCase):
	def setUp(self):
		self.size = 15
		self.queue = Queue(self.size)

	def testFULL(self):
		self.assertFalse(self.queue.is_full())
        	for x in range(self.size):
            		self.queue.put(x)
		self.assertTrue(self.queue.is_full())
		self.queue.get()
		self.assertFalse(self.queue.is_full())
	
	def testEMPTY(self):
		self.assertTrue(self.queue.is_empty())
		self.queue.put(1)
		self.assertFalse(self.queue.is_empty())
		self.queue.get()
		self.assertTrue(self.queue.is_empty())

	def testPUT(self):
		self.assertTrue(self.queue.is_empty())
		for x in range(self.size):
			self.queue.put(x+10)
		self.assertTrue(self.queue.is_full())
		self.assertRaises(IndexError, lambda: self.queue.put(1000))

	def testGET(self):
		self.assertRaises(IndexError, lambda: self.queue.get())
		self.assertRaises(IndexError, lambda: self.queue.get())
		self.assertRaises(IndexError, lambda: self.queue.get())
		self.queue.put(2+10)
		self.queue.get()
		self.assertRaises(IndexError, lambda: self.queue.get())
		for x in range(self.size-1):
			self.queue.put(x+10)
		for x in range(self.size - 1):
			self.queue.get()
		self.assertRaises(IndexError, lambda: self.queue.get())

	def testCOMBO(self):
		self.assertTrue(self.queue.is_empty())
		self.assertFalse(self.queue.is_full())
		for x in range(self.size):
            		self.queue.put(x)
		self.assertRaises(IndexError, lambda: self.queue.put(1000))
		self.assertTrue(self.queue.is_full())
		self.queue.get()
		self.queue.put(88)
		self.assertRaises(IndexError, lambda: self.queue.put(1000))
		self.assertTrue(self.queue.is_full())
		for x in range(self.size):
			self.queue.get()
        	for x in range(self.size):
            		self.queue.put(x)
		self.assertRaises(IndexError, lambda: self.queue.put(1000))
		self.assertRaises(IndexError, lambda: self.queue.put(1000))
		for x in range(self.size):
			self.queue.get()
		self.assertRaises(IndexError, lambda: self.queue.get())
		self.queue.put(1)
		self.queue.get()
		self.assertTrue(self.queue.is_empty())
	
if __name__ == '__main__':
	unittest.main()  # uruchamia wszystkie testy
