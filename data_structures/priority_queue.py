###############################
# priority queue
# pros : 
# - 
# 
# cons:
# - 
#
# time complexity : 
# space complexity : 
###############################

from queue import Queue
from linked_list import Linked_list, Node

class PriorityQueue (Queue):
	def __init__ (self, key_name):
		Queue.__init__(self)
		self.key_name = key_name

	def push (self, value): 
		new_node = Node(value)

		curr_node = self.head.next

		while curr_node != self.tail:
			if getattr(curr_node.value, self.key_name) >= getattr(new_node.value, self.key_name):
				prev_node = curr_node.prev

				prev_node.next = new_node
				new_node.prev = prev_node

				new_node.next = curr_node
				curr_node.prev = new_node

				self.size += 1

				return

			curr_node = curr_node.next

		Queue.add_to_tail(self, value)


	def pop_min (self):
		return Linked_list.remove_from_head(self)

	def pop_max (self):
		return Linked_list.remove_from_tail(self)


################################################################################################################
# test cases
################################################################################################################

def main():
	testcase_1()


def testcase_1():
	priorityqueue = PriorityQueue("value")

	input_list = [1,3,5,7,9,2,4,6,8,10]
	new_input_list = []

	for input in input_list:
		new_input_list.append(Node(input))

	min_priority_queue = []
	max_priority_queue = []

	for x in new_input_list:
		priorityqueue.push(x)

	for x in range(len(new_input_list)):
		min_priority_queue.append(priorityqueue.pop_min().value)

	for x in new_input_list:
		priorityqueue.push(x)

	for x in range(len(new_input_list)):
		max_priority_queue.append(priorityqueue.pop_max().value)


	print min_priority_queue
	print max_priority_queue

if __name__ == "__main__":
	main()








