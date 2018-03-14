###############################
# Longest Increasing Subsequence
#
# time complexity : 
# space complexity : 
###############################


def longest_increasing_subsequence_dp (input_list):

	def longest_increasing_subsequence (i):

		if dp[i] != None:
			return dp[i]

		max_lentgth = 0

		for k in range(0, i):
			if input_list[k] < input_list[i]:
				if max_lentgth < longest_increasing_subsequence(k):
					max_lentgth = longest_increasing_subsequence(k)
				
		dp[i] = max_lentgth + 1
		return dp[i]

	dp = [None] * len(input_list)
	longest_increasing_subsequence( len(input_list)-1 )
	return dp

def main():
	input_list = [1,4,2,6,7,9,3,4,6,4,9,10]
	print input_list
	print longest_increasing_subsequence_dp(input_list)

if __name__ == "__main__":
	main()