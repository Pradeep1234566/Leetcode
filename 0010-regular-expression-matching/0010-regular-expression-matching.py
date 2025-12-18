class Solution(object):
   
    def helper(self, s, p, i, j, dp):
        if i == 0 and j == 0:
            return True
        
        if j == 0:
            return False
        
        if dp[i][j] != -1:
            return dp[i][j]

        if p[j-1] == '*':
            zero = self.helper(s, p, i, j-2, dp)

            one = False
            if i > 0 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                one = self.helper(s, p, i-1, j, dp)

            dp[i][j] = zero or one
            return dp[i][j]

        if i > 0 and (s[i-1] == p[j-1] or p[j-1] == '.'):
            dp[i][j] = self.helper(s, p, i-1, j-1, dp)
            return dp[i][j]

        dp[i][j] = False
        return False



    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = [[-1] *(m+1) for _ in range(n+1)]
        return self.helper(s, p, n, m, dp)
        