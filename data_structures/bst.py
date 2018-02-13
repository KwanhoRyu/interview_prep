###############################
# heap
# useful cases : good space complexity
#
# time complexity : build -> O(nlogn)
# space complexity : O(n)
###############################

class NodeForPrimitiveDataTypes:
	def __init__ (self, value):
		self.value = value

class BSTNode:
	def __init__(self, value):
		self.value = value
		self.l_child = None
		self.r_child = None

class BST:

	def __init__(self, key_name):
		self.root = None
		self.key_name = key_name

	def insert(self, value):
		new_node = BSTNode(value)
		if self.root == None:
			self.root = new_node
			return

		self.compare_and_insert(self.root, new_node)

#	def remove ():


	def compare_and_insert (self, current_node, new_node):
		if getattr(current_node.value, self.key_name) >= getattr(new_node.value, self.key_name):
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

		self.traverse(return_array, self.root)

		return return_array

	def traverse (self, return_array, node):
		if node == None:
			return

		self.traverse(return_array, node.l_child)
		return_array.append( getattr(node.value, self.key_name) )
		self.traverse(return_array, node.r_child)


################################################################################################################
# test cases
################################################################################################################

def main():
	input_array = [9, 7, 5, 3, 1]
	expected_output = [1, 3, 5, 7, 9]
	

	input_array = [9, 3, 5, 7, 1]
	print ( sort_using_bst(input_array) )

	input_array = [1, 2, 1, 1, 9, 3, 5, 7, 1]
	print ( sort_using_bst(input_array) )

if __name__ == "__main__":
	main()




