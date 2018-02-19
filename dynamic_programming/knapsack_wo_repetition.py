###############################
# Knapsack with repetition
#
# time complexity : 
# space complexity : 
###############################

def knapsack_wo_repetition_dp (weights, values, W):

	def knapsack (w, i):
		# base case
		if w == 0:
			return 0

		if i == -1:
			return 0

		# look up dp table
		if dp[w][i] != None:
			return dp[w][i]

		# dp formula
		max_value = knapsack(w, i-1)
		
		if weights[i] <= w:
			if max_value <= knapsack(w - weights[i], i-1) + values[i]:
				max_value = knapsack(w - weights[i], i-1) + values[i]
		dp[w][i] = max_value

		return dp[w][i]

	dp = [ [None] * len(weights) for x in range(W+1) ]
	for i in range(len(weights)):
		dp[0][i] = 0
	knapsack(W, len(weights)-1)
	return dp



def main():
	weights = [3,4,5]
	values = [3,4,4]
	W = 8
	print weights
	print values
	print W
	print "--- DP table ---"
	dp = knapsack_wo_repetition_dp(weights, values, W)
	for w in dp:
		print w

if __name__ == "__main__":
	main()