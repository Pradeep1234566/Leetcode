class Solution(object):
    def helper(self, s, t, i, j, dp):
        if i == len(t):
            return 1
        if j == len(s):
            return 0
        
        if (i, j) in dp:
            return dp[(i,j)]

        
        if s[j] == t[i]:
            include = self.helper(s,t,i+1,j+1,dp)
            exclude = self.helper(s,t,i,j+1,dp)
            dp[(i,j)] = include + exclude
        
        else:
            dp[(i,j)] = self.helper(s,t,i,j+1,dp)
        
        return dp[(i,j)]

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        dp = {}

        return self.helper(s,t,i,j,dp)