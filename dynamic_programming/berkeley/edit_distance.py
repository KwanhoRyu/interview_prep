###############################
# Edit Distance
#
# time complexity : 
# space complexity : 
###############################

def edit_distance_dp (word1, word2):

	def diff(i, j):
		if word1[i] == word2[j]:
			return 0
		else:
			return 1

	def edit_distance (i, j):
		# base case
		if i < 0 and j < 0:
			return 0
		if i < 0:
			return j+1
		if j < 0:
			return i+1

		# look up dp table
		if dp[i][j] != None:
			return dp[i][j]

		# dp formula
		dp[i][j] = min( edit_distance(i-1, j) + 1, edit_distance(i, j-1) + 1, edit_distance(i-1, j-1) + diff(i, j) )

		return dp[i][j]

	dp = [ [None] * len(word2) for x in range(len(word1)) ]
	edit_distance(len(word1)-1, len(word2)-1)
	return dp



def main():
	word1 = 'kitten'
	word2 = 'sitting'
	print word1
	print word2
	print "--- DP table ---"

	dp = edit_distance_dp(word1, word2)
	for i in dp:
		print i

if __name__ == "__main__":
	main()