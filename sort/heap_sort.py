###############################
# heap
# useful cases : good space complexity
#
# time complexity : build -> O(nlogn)
# space complexity : O(n)
###############################

import sys
sys.path.insert(0, '/Users/kwanhoryu/study/interview_prep/data_structures')

from min_heap import NodeForPrimitiveDataTypes, MinHeap

def heap_sort (int_array):
	minheap = MinHeap("value")

	for x in int_array:
		minheap.push( NodeForPrimitiveDataTypes(x) )

	return minheap.get_sorted_list()


################################################################################################################
# test cases
################################################################################################################

def main():
	pass


if __name__ == "__main__":
	main()


















