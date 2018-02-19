###############################
# Knapsack with repetition
#
# time complexity : 
# space complexity : 
###############################

def knapsack_w_repetition_dp (weights, values, W):

	def knapsack (w):
		# base case
		if w == 0:
			return 0

		# look up dp table
		if dp[w] != None:
			return dp[w]

		# dp formula
		max_value = 0
		for i in range(len(weights)):
			if weights[i] <= w:
				if max_value <= knapsack(w - weights[i]) + values[i]:
					max_value = knapsack(w - weights[i]) + values[i]
		dp[w] = max_value

		return dp[w]

	dp = [None] * (W+1)
	knapsack(W)
	return dp

#	dp = [ [None] * input_integer for x in range(input_integer) ]

def main():
	weights = [3,4,5]
	values = [3,4,4]
	W = 15
	print weights
	print values
	print W
	print knapsack_w_repetition_dp(weights, values, W)

if __name__ == "__main__":
	main()