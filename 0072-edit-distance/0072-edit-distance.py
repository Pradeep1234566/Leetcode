class Solution(object):
    def helper(self, word1, word2, n, m, dp):
        if n == 0:
            return m
        
        if m == 0:
            return n

        if dp[n][m] != -1:
            return dp[n][m]
        
        if word1[n-1] == word2[m-1]:
            dp[n][m] = self.helper(word1, word2, n-1, m-1, dp)
        
        else:
            insert = 1 + self.helper(word1, word2, n, m-1, dp)
            deletion = 1 + self.helper(word1, word2, n-1, m, dp)
            replace = 1+ self.helper(word1, word2, n-1, m-1, dp)

            dp[n][m] = min(insert, deletion, replace)

        
        return dp[n][m]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        dp = [[-1]*(m+1) for _ in range(n+1)]

        return self.helper(word1, word2, n, m, dp)


        