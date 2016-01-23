# v.3.0
class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

	@staticmethod
	def remove_head(node):	
		try:
			if node is None:
				raise Exception("pusta lista")
			if (node.data) is None:
				raise Exception("pusta lista")
			if (node.next) is None:
				node.data = None
				node.next = None
			else:
				if(node.next is 0):
					node.data = None
					node.next = None
				else:
					helperA = node.next
					helper = node.next.next
					node.data = helperA
					node.next = helper
					return node
		except Exception:
			print("Lista jest pusta")
		
	@staticmethod
	def remove_tail(node):
		try:
			if node is None:
				raise Exception()
			if (node.data) is None:
				raise Exception()
			if (node.next) is None:
				node.data = None
				node.next = None
			else:
				if(node.next is 0):
					node.data = None
					node.next = None
				else:
					lastOne = 0
					beforeLastOne = 0
					while node:
						beforeLastOne = lastOne
						lastOne = node
						node = node.next
					beforeLastOne.next = 0
					return node
		except Exception:
			print("Lista jest pusta")
