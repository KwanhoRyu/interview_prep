###############################
# merge_sort
# useful cases: good time complexity
#
# time complexity: O(nlogn)
# space complexity: O(n)
###############################

def merge_sort (array):

	if len(array) == 1:
		return array

	pivot_index = len(array)/2

	array_l = array[:pivot_index]
	array_r = array[pivot_index:]

	sorted_array_l = merge_sort(array_l)
	sorted_array_r = merge_sort(array_r)

	merged_array = []
	array_l_index = 0
	array_r_index = 0

	while  (array_l_index < len(sorted_array_l)) and (array_r_index < len(sorted_array_r)):
		# the element from left the array is smaller
		if sorted_array_l[array_l_index] <= sorted_array_r[array_r_index]:
			merged_array.append( sorted_array_l[array_l_index] )
			array_l_index += 1

		# the element from the right array is smaller
		else:
			merged_array.append( sorted_array_r[array_r_index] )
			array_r_index += 1

	# append the array with unused elements to the result array
	merged_array = merged_array + sorted_array_l[array_l_index:] + sorted_array_r[array_r_index:]

	return merged_array


################################################################################################################
# test cases
################################################################################################################

def main():
	pass


if __name__ == "__main__":
	main()
