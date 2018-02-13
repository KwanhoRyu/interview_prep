###############################
# heap
# useful cases : good space complexity
#
# time complexity : build -> O(nlogn)
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


	def traverse_BST (self):
		return_array = []

		self.visit(return_array, self.root)

		return return_array

	def visit (self, return_array, node):

		if node == None:
			return

		self.visit(return_array, node.l_child)
		return_array.append(node.value)
		self.visit(return_array, node.r_child)


def sort_using_bst (array):
	bst = BST()

	for x in array:
		bst.insert(x)

	return bst.traverse_BST()



################################################################################################################

input_array = [9, 7, 5, 3, 1]
expected_output = [1, 3, 5, 7, 9]
print ( sort_using_bst(input_array) == expected_output )

input_array = [9, 3, 5, 7, 1]
print ( sort_using_bst(input_array) )

input_array = [1, 2, 1, 1, 9, 3, 5, 7, 1]
print ( sort_using_bst(input_array) )





