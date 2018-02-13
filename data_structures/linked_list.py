###############################
# Linked List
# pros : 
# - dynamically increase and decrease memory space according to data
# - insertion/deletion in O(1) (only if you know where the node to be inserted/deleted is located at)
# 
# cons:
# - lookup in O(n) (might have to check the entire list)
#
# time complexity : 
# space complexity : O(n)
###############################

class NodeForPrimitiveDataTypes:
	def __init__ (self, value):
		self.value = value

class LinkedListNode:
	def __init__ (self, value=None, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

class Linked_list:

	def __init__ (self):
		self.head = LinkedListNode()
		self.tail = LinkedListNode()

		self.head.next = self.tail
		self.tail.prev = self.head

		self.size = 0

	def add_to_head (self, value):
		new_node = LinkedListNode(value)

		new_node.next = self.head.next
		new_node.next.prev = new_node

		self.head.next = new_node
		new_node.prev = self.head

		self.size += 1

	def add_to_tail (self, value):
		new_node = LinkedListNode(value)

		new_node.prev = self.tail.prev
		new_node.prev.next = new_node
		
		self.tail.prev = new_node
		new_node.next = self.tail

		self.size += 1

	def remove_from_head (self):
		if self.size == 0:
			return
		
		return_value = self.head.next.value

		self.head.next = self.head.next.next
		self.head.next.prev = self.head

		self.size -= 1

		return return_value

	def remove_from_tail (self):
		if self.size == 0:
			return

		return_value = self.tail.prev.value
	
		self.tail.prev = self.tail.prev.prev
		self.tail.prev.next = self.tail

		self.size -= 1

		return return_value

	def is_empty (self):
		return self.size == 0

	def travese_list (self):
		curr_node = self.head.next
		return_array = []

		while curr_node != self.tail:
			return_array.append(curr_node.value.value)
			curr_node = curr_node.next

		return return_array


################################################################################################################
# test cases
################################################################################################################

def main():
	LL = Linked_list()

	LL.add_to_head(NodeForPrimitiveDataTypes(1))
	LL.remove_from_tail()
	LL.remove_from_tail()  
	LL.add_to_head(NodeForPrimitiveDataTypes(2))
	LL.add_to_tail(NodeForPrimitiveDataTypes(7))
	LL.add_to_head(NodeForPrimitiveDataTypes(3))
	LL.add_to_tail(NodeForPrimitiveDataTypes(4))
	LL.remove_from_tail()
	print(LL.size)


	print (LL.travese_list())

if __name__ == "__main__":
	main()


