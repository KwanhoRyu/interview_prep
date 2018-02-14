###############################
# Fibonacci
#
# time complexity : 
# space complexity : 
###############################


def fibonacci_dp (n):

	def fibonacci (n):
		if n <= 0:
			return 0

		if dp[n] != None:
			return dp[n]
	
		dp[n] = fibonacci(n-1) + fibonacci(n-2)
		return dp[n]

	dp = [None] * (n+1)
	dp[1] = dp[2] = 1

	fibonacci(n)
	return dp

def main():
	print fibonacci_dp(5)

if __name__ == "__main__":
	main()