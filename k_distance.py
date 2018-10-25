def can_k_distance(s,t,k):

	s_l = len(s)
	t_l = len(t)

	dp = [[0 for _ in xrange(s_l+1)] for _ in xrange(t_l+1)]
	for i in xrange(1,s_l+1):
		dp[0][i] = 1 + dp[0][i-1]
	for j in xrange(1,t_l+1):
		dp[j][0] = 1 + dp[j-1][0]

	for i in xrange(1,t_l+1):
		for j in xrange(1,s_l+1):
			if t[i-1] == s[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j],dp[i][j-1]))
				
	if dp[-1][-1] <= k:
		return True
	else:
		return False



