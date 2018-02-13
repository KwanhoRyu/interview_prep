from bst_sort import bst_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort import quick_sort

def main():

	testcases = [ ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9]), 
				([9, 3, 5, 7, 1], [1, 3, 5, 7, 9]),
				([1, 2, 1, 1, 9, 3, 5, 7, 1], [1, 1, 1, 1, 2, 3, 5, 7, 9])
				]

	for index, (input_array, expected_output) in enumerate(testcases):
		testcase(index, input_array, expected_output)

def testcase(index, input_array, expected_output):
	print("\n-- testcase {} --".format(index))

	input_array_copy = input_array

	print ("input array : {}".format(input_array))
	print ("expected output : {}\n".format(expected_output))

	# bst sort
	bst_sort_result = bst_sort(input_array)
	print ( "bst sort: {}, {}".format(bst_sort_result, bst_sort_result == expected_output) )

	# merge sort
	merge_sort_result = merge_sort(input_array)
	print ( "merge sort: {}, {}".format(merge_sort_result, merge_sort_result == expected_output) )

	# quick sort
	quick_sort(input_array, 0, len(input_array)-1)
	print ( "quick sort: {}, {}".format(input_array, input_array == expected_output) )
	input_array = input_array_copy

	# heap sort
	heap_sort_result = heap_sort(input_array)
	print ( "heap sort: {}, {}".format(heap_sort_result, heap_sort_result == expected_output) )


if __name__ == "__main__":
	main()








