###############################
# Longest Palindromic_Subsequence
#
# time complexity : 
# space complexity : 
###############################

def lps_dp (word):

	def diff(i, j):
		if word[i] == word[j]:
			return 2
		else:
			return 0

	def lps (i, j):
		# base case
		if i > j:
			return 0
		if i == j:
			dp[i][j] = 1
			return dp[i][j]

		# look up dp table
		if dp[i][j] != None:
			return dp[i][j]

		# dp formula
		dp[i][j] = max( lps(i+1, j), lps(i, j-1), lps(i+1, j-1) + diff(i, j) )

		return dp[i][j]

	dp = [ [None] * len(word) for x in range(len(word)) ]
	lps(0, len(word)-1)
	return dp



def main():
	word = 'bbbab'
	print word
	print "--- DP table ---"

	dp = lps_dp(word)
	for i in dp:
		print i

if __name__ == "__main__":
	main()