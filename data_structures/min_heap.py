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

class MinHeap:
	def __init__ (self, key_name):	
		self.minHeapArray = []
		self.size = 0
		self.key_name = key_name

	def push (self, node):
		self.minHeapArray.append(node)
		self.size += 1

		self.bubble_up(self.size-1)

	def pop (self):
		if self.size == 0:
			print("heap is empty")
			return

		return_node = self.minHeapArray[0]
		last_element = self.minHeapArray.pop()
		self.size -= 1

		if not self.is_empty():
			self.minHeapArray[0] = last_element
			self.sift_down(0)

		return return_node

	def get_min (self):
		if self.is_empty():
			print("heap is empty")
			return
		return self.minHeapArray[0]

	def get_sorted_list(self):
		sorted_list = []

		while not self.is_empty():
			node = self.pop()
			sorted_list.append( getattr(node, self.key_name) )

		return sorted_list

	def update_key (self, index, new_key):
		old_key = getattr(self.minHeapArray[index], self.key_name)
		setattr(self.minHeapArray[index], self.key_name, new_key)

		if old_key < new_key:
			self.sift_down(index)
		else:
			self.bubble_up(index)

	def bubble_up (self, index):
		# base cases: when reaching the root node
		if index == 0:
			return

		parent_index = (index-1)/2
		# compare current node's value with its parent's value
		if getattr(self.minHeapArray[parent_index], self.key_name) > getattr(self.minHeapArray[index], self.key_name):
			self.swap(parent_index, index)
			self.bubble_up(parent_index)

	def sift_down (self, index):
		l_child_index, r_child_index = index*2+1, index*2+2

		# base cases: when current node is a leaf node
		if (l_child_index > self.size-1):
			return

		smaller_node_index = self.find_smaller_node(l_child_index, r_child_index)
		# compare current node's value with its smaller child's value
		if getattr(self.minHeapArray[index], self.key_name) > getattr(self.minHeapArray[smaller_node_index], self.key_name):
			self.swap(smaller_node_index, index)
			self.sift_down(smaller_node_index)

	def swap (self, s, t):
		temp = self.minHeapArray[t]
		self.minHeapArray[t] = self.minHeapArray[s]
		self.minHeapArray[s] = temp

	def find_smaller_node (self, l_index, r_index):
		if (r_index > self.size-1) or ( getattr(self.minHeapArray[l_index], self.key_name) <= getattr(self.minHeapArray[r_index], self.key_name) ):
			return l_index
		else:
			return r_index

	def is_empty (self):
		return self.size == 0

	def find_index (self, value):
		for index in range(0, self.size):
			if self.minHeapArray[index] == value:
				return index
		return None

	def print_min_heap_array (self):
		return_list = []

		for x in self.minHeapArray:
			return_list.append( getattr(x, self.key_name) )

		return return_list

################################################################################################################
# test cases
################################################################################################################

def main():
	testcase_1()


def testcase_1():

	node1 = NodeForPrimitiveDataTypes(1)
	node2 = NodeForPrimitiveDataTypes(2)
	node3 = NodeForPrimitiveDataTypes(3)
	node4 = NodeForPrimitiveDataTypes(4)
	node5 = NodeForPrimitiveDataTypes(5)
	node6 = NodeForPrimitiveDataTypes(6)

	minheap = MinHeap("value")

	minheap.push(node3)
	minheap.push(node4)
	minheap.push(node1)
	minheap.push(node2)
	minheap.push(node6)
	minheap.push(node5)

	print(minheap.print_min_heap_array())
	print(minheap.find_index(node3))

	minheap.update_key(0, 9)
	print(minheap.print_min_heap_array())



#	minheap.pop()
#	print(minheap.print_min_heap_array())
	
	print(minheap.get_sorted_list())



	# print(minheap.pop().value)
	# print(minheap.pop().value)
	# print(minheap.pop().value)
	# print(minheap.pop().value)



if __name__ == "__main__":
	main()




















