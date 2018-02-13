###############################
# sort using binary search tree
# useful cases : when data is streaming in
#
# time complexity : build -> O(n^2)
# space complexity : O(n)
###############################

class Node:
	def __init__(self, value):
		self.value = value
		self.l_child = None
		self.r_child = None

class BST:

	def __init__(self):
		self.root = None


	def insert(self, value):
		new_node = Node(value)
		if self.root == None:
			self.root = new_node
			return

		self.compare_and_insert(self.root, new_node)


#	def remove ():


	def compare_and_insert (self, current_node, new_node):
		if current_node.value >= new_node.value:
			if current_node.l_child == None:
				current_node.l_child = new_node
			else:
				self.compare_and_insert(current_node.l_child, new_node)
		else:
			if current_node.r_child == None:
				current_node.r_child = new_node
			else:
				self.compare_and_insert(current_node.r_child, new_node)


	def serialize (self):
		return_array = []

		self.visit(return_array, self.root)

		return return_array

	def visit (self, return_array, node):

		if node == None:
			return

		self.visit(return_array, node.l_child)
		return_array.append(node.value)
		self.visit(return_array, node.r_child)


def bst_sort (array):
	bst = BST()

	for x in array:
		bst.insert(x)

	return bst.serialize()



################################################################################################################
# test cases
################################################################################################################

def main():
	pass

if __name__ == "__main__":
	main()





