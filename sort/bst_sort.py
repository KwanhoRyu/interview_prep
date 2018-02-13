###############################
# sort using binary search tree
# useful cases : when data is streaming in
#
# time complexity : build -> O(n^2)
# space complexity : O(n)
###############################

import sys
sys.path.insert(0, '/Users/kwanhoryu/study/interview_prep/data_structures')

from bst import NodeForPrimitiveDataTypes, BSTNode, BST

def bst_sort (array):
	bst = BST("value")

	for x in array:
		bst.insert(NodeForPrimitiveDataTypes(x))

	return bst.serialize()


################################################################################################################
# test cases
################################################################################################################

def main():
	pass

if __name__ == "__main__":
	main()





