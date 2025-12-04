class Solution(object):
    def helper(self, s, p, i, j, dp):
        # Both s and p consumed
        if i == 0 and j == 0:
            return True
        
        # Pattern consumed but string still left
        if j == 0:
            return False
        
        # String consumed but pattern left
        if i == 0:
            # Valid only if remaining pattern is all '*'
            return all(x == '*' for x in p[:j])

        if dp[i][j] != -1:
            return dp[i][j]

        # Case 1: direct match or '?'
        if s[i-1] == p[j-1] or p[j-1] == '?':
            dp[i][j] = self.helper(s, p, i-1, j-1, dp)
            return dp[i][j]

        # Case 2: pattern has '*'
        if p[j-1] == '*':
            # Two choices:
            # 1️⃣ '*' acts as empty → move pattern
            # 2️⃣ '*' consumes s[i-1] → move string
            dp[i][j] = ( self.helper(s, p, i, j-1, dp)  # '*' = empty
                         or
                         self.helper(s, p, i-1, j, dp) ) # '*' consumes a char
            
            return dp[i][j]

        dp[i][j] = False
        return dp[i][j]


    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        return self.helper(s, p, n, m, dp)
