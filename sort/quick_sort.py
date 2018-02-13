###############################
# quick_sort
# useful cases : good space complexity
#
# time complexity : with good pick of median -> O(nlogn), worst case -> O(n^2)
# space complexity : O(1)
###############################

def quick_sort (array, start, end):

	# base cases: when onlt one element left 
	if (start == end):
		return 

	pivot_index = partition(array, start, end)

	if start != pivot_index:
		quick_sort(array, start, pivot_index - 1)
	if end != pivot_index:
		quick_sort(array, pivot_index + 1, end)

	return

# partion -> O(n) time operation
def partition (array, start, end):
	pivot_value = array[end]
	pivot_index = start

	for i in range(start, end):
		if array[i] <= pivot_value:
			swap(array, i, pivot_index)
			pivot_index += 1

	swap(array, pivot_index, end)

	return pivot_index

def swap (array, s, t):
	if s == t:
		return

	temp = array[t]
	array[t] = array[s]
	array[s] = temp
	return


################################################################################################################
# test cases
################################################################################################################

def main():
	pass

if __name__ == "__main__":
	main()


