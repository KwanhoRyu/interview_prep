# Binary Search
#
# return index of the target in the given sorted array. 
# If target does not exist, return -1.
#
# i.e.,
# input : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7
# output : 6


def binary_search (array, start, end, target):

	if (start == end) and array[start] != target:
		return -1

	# compare pivot with target
	pivot_index = start + (end-start)/2
	if array[pivot_index] == target:
		return pivot_index

	elif array[pivot_index] > target:
		return binary_search(array, start, pivot_index, target)

	else:
		return binary_search(array, pivot_index + 1, end, target)

################################################################################################################

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
print(binary_search(input_array, 0, len(input_array)-1, target))

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11
print(binary_search(input_array, 0, len(input_array)-1, target))

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 0
print(binary_search(input_array, 0, len(input_array)-1, target))