# v.2.0
class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

	@staticmethod
	def remove_head(node):
		helperA = node.next
		helper = node.next.next
		node.data = helperA
		node.next = helper
		res = Node(node.data, node.next)
		return res
		
	@staticmethod
	def remove_tail(node):
		lastOne = 0
		beforeLastOne = 0
		while node:
			beforeLastOne = lastOne
			lastOne = node
			node = node.next
		beforeLastOne.next = 0
		res = Node(beforeLastOne.data, beforeLastOne.next)
		return res

test = None
test = Node(1, test)
test = Node(2, test)
test = Node(3, test)
Node.remove_tail(test)
Node.remove_head(test)
while test:
	print test.data
	test = test.next