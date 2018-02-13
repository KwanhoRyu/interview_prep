###############################
# stack
# pros : 
# - 
# 
# cons:
# - 
#
# time complexity : 
# space complexity : 
###############################

class Stack:

	def __init__ (self):
		self.stack = []
		self.size = 0

	def push (self, value):
		self.stack.append(value)
		self.size += 1

	def pop (self):
		if self.size ==0:
			return

		return_value = self.stack.pop()
		self.size -= 1

		return return_value


################################################################################################################
# test cases
################################################################################################################

def main():
	stack = Stack()

	input_list = range (1, 10)
	output_list = []

	for x in input_list:
		stack.push(x)


	for x in range(1,11):
		output_list.append(stack.pop())

	print output_list


if __name__ == "__main__":
	main()