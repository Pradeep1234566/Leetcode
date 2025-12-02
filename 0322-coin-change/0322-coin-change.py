class Solution(object):
    def recur(self, coins, i, amount, dp):
        if amount == 0:
            return 0
        if amount < 0 or i < 0:
            return float('inf')

        if dp[i][amount] != -1:
            return dp[i][amount]

        # include the coin
        include = 1 + self.recur(coins, i, amount - coins[i], dp)

        # exclude the coin
        exclude = self.recur(coins, i - 1, amount, dp)

        dp[i][amount] = min(include, exclude)
        return dp[i][amount]

    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        ans = self.recur(coins, n - 1, amount, dp)

        return -1 if ans == float('inf') else ans
