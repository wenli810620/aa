#coin change 
#what's the minimum length of one of the comb
def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1 for _ in xrange(amount+1)]
        dp[0] = 0
        for c in coins:
            for t in xrange(c,amount+1):
                dp[t] = min((dp[t-c]+1,dp[t]))
       
        if dp[-1] > amount : return -1
        else:
            return dp[-1]

#how many combinations 
def coinChange2(coins, amount):
    dp = [0 for _ in xrange(amount+1)]
    dp[0] = 1
    for c in coins:
        for t in xrange(c,amount+1):
            dp[t] += dp[t-c]
    return dp[-1]
    



    