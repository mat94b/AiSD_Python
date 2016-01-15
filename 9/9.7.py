class Node:
	def __init__(self, data=None, l=None, r=None):
		self.data = data
		self.left = l
		self.right = r

	def __str__(self):
		return str(self.data)

	def insert_bst(self, data):
		if self.data is None:
			self.data = data
		elif self.data > data:  
			if self.left:
				self.left.insert_bst(data)
			else:
				self.left = Node(data)
		elif self.data < data:  
			if self.right:
				self.right.insert_bst(data)
			else:
				self.right = Node(data)
		else:
            		print("Liczba "+str(data)+" - juz zostala zapisana do drzewa wczesniej")
			pass

def count_total(counter):
	sumaResult = None
	if counter is not None:
		sumaResult = count_total(counter.left) 
		sumaResult += count_total(counter.right)
		sumaResult += counter.data
		return sumaResult
	elif counter is None:
		return 0

def count_leafs(counter):
	sumaResult = 0
	if counter is None:
		return 0
	ri = counter.right
	le = counter.left
	if ri is None and le is None:
		sumaResult += count_leafs(le)
		sumaResult += count_leafs(ri)
		sumaResult += 1
		return sumaResult
	else:
		sumaResult += count_leafs(le)
		sumaResult += count_leafs(ri)
		return sumaResult

def testFunction():
	tree = Node()
	tree.insert_bst(0)
	tree.insert_bst(1)
	tree.insert_bst(2)
	tree.insert_bst(3)
	tree.insert_bst(4)
	tree.insert_bst(5)
	tree.insert_bst(6)
	tree.insert_bst(7)
	tree.insert_bst(8)
	tree.insert_bst(9)
	tree.insert_bst(10)
	tree.insert_bst(-1)
	tree.insert_bst(-2)
	tree.insert_bst(-12)
	tree.insert_bst(-9)
	print("+---------------------------------------------+")
	print("|                                             |")
	print("|     SUMA WSZYSTKIEGO: "+str(count_total(tree))+"                    |")
	print("|     ILOSC LISCI: "+str(count_leafs(tree))+"                          |")
	print("|                                             |")
	print("+---------------------------------------------+")

testFunction()
