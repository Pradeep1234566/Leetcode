class Solution(object):
    def recur(self, amount, coins, N, dp):
        if amount == 0:
            return 1

        if amount < 0 or N < 0:
            return 0

        if dp[N][amount] != -1:
            return dp[N][amount]

        if coins[N] <= amount:
            include = self.recur(amount-coins[N], coins, N, dp)
            exclude = self.recur(amount, coins, N-1, dp)
            dp[N][amount] = include + exclude
            
        else:
            dp[N][amount] = self.recur(amount, coins, N-1, dp)

        return dp[N][amount]

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        N = len(coins)

        dp = [[-1]*(amount+1) for _ in range(N+1)] 

        return self.recur(amount, coins, N-1, dp)

        