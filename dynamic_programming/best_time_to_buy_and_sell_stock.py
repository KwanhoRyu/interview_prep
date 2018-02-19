###############################
# Best time to buy and sell stock
#
# time complexity : 
# space complexity : 
###############################

def bttbass_dp (input_list):

	def bttbass (i, j):
		# base case
		if i == j:
			return 0

		# look up dp table
		if dp[i][j] != None:
			return dp[i][j]

		# dp formula
		max_value = 0
		if input_list[j] - input_list[i] > 0:
			max_value = input_list[j] - input_list[i]

		for k in range(i,j):
			if max_value < bttbass(i, k) + bttbass(k+1, j):
				max_value = bttbass(i, k) + bttbass(k+1, j)
		dp[i][j] = max_value

		return dp[i][j]

	dp = [ [None] * len(input_list) for x in range(len(input_list)) ]
	bttbass(0, len(input_list)-1)
	return dp



def main():
	input_list = [9,2,5,2,4,3,6,10,6,3]
	print input_list
	print "--- DP table ---"
	dp = bttbass_dp(input_list)
	for i in dp:
		print i

if __name__ == "__main__":
	main()