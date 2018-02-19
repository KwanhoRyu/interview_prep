###############################
# Integer Break
#
# time complexity : 
# space complexity : 
###############################

def integer_break_dp (input_integer):

	def integer_break (i):
		# base case
		if i == 1 :
			return 1

		# look up dp table
		if dp[i] != None:
			return dp[i]

		# dp formula
		max_product = i
		for k in range(1, (i/2)+1):
			if max_product < integer_break(k) * integer_break(i-k):
				max_product = integer_break(k) * integer_break(i-k)
		dp[i] = max_product

		return dp[i]

	dp = [None] * (input_integer+1)
	integer_break(input_integer)
	return dp

#	dp = [ [None] * input_integer for x in range(input_integer) ]


def main():
	input_integer = 10
	print input_integer
	print integer_break_dp(input_integer)

if __name__ == "__main__":
	main()