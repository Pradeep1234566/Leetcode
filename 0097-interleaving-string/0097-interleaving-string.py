class Solution(object):
    def helper(self, s1, s2, s3, n, m, memo):
        # base case
        if n == 0 and m == 0:
            return True
        
        if (n, m) in memo:
            return memo[(n, m)]

        valid = False
        k = n + m - 1  # index in s3

        # take from s1
        if n > 0 and s1[n-1] == s3[k]:
            valid = self.helper(s1, s2, s3, n-1, m, memo)
        
        # take from s2
        if not valid and m > 0 and s2[m-1] == s3[k]:
            valid = self.helper(s1, s2, s3, n, m-1, memo)

        memo[(n, m)] = valid
        return valid
        
    def isInterleave(self, s1, s2, s3):
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        memo = {}
        return self.helper(s1, s2, s3, n, m, memo)
