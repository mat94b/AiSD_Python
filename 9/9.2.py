class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

	def print_list(node):
		print("L: ")
		while node:
			print(node)
			node = node.next
		print()

	@staticmethod
	def merge(node1, node2):
		if(node1 is None) and (node2 is None):
			return None
		elif(node1 is None):
			node1 = node2
			return node1
		head = node1
		last = None
		while node1:
			last = node1
			node1 = node1.next
		last.next = node2
		return Node(head.data, head.next)
