###############################
# queue
# pros : 
# - 
# 
# cons:
# - 
#
# time complexity : 
# space complexity : 
###############################

from linked_list import Node, Linked_list

class Queue (Linked_list):
	def __init__ (self):
		Linked_list.__init__(self)

	def push (self, value):
		Linked_list.add_to_tail(self, value)

	def pop (self):
		if self.size ==0:
			return None
			
		return_value = Linked_list.remove_from_head(self)
		return return_value

################################################################################################################
# test cases
################################################################################################################

def main():
	queue = Queue()

	input_list = []
	for x in range (1, 10):
		input_list.append(Node(x))

	output_list = []

	for x in input_list:
		queue.push(x)

	while not queue.is_empty():
		output_list.append(queue.pop().value)

	print output_list


if __name__ == "__main__":
	main()