# v.2.0
import random

class RandomQueue:
	def __init__(self):
		self.maximum=20
		self.listOfElements = list()
		self.n = 0

	def is_empty(self):
		if not self.listOfElements:
			return True
		else:
			return False

	def is_full(self):
		if self.listOfElements is self.maximum:
			return True
		else:
			return False

	def insert(self, item):
		if self.n is self.maximum:
			raise IndexError
		self.n+=1
		self.listOfElements.append(item)

	def remove(self):
		if not self.listOfElements:
			raise IndexError
		self.n -= 1
		helper = random.randint(0, self.n)
		result = self.listOfElements[helper]
		del listOfElements[helper]
		return result
