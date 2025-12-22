class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        memo = {}

        def helper(i):
            # fully decoded
            if i == n:
                return 1
            
            # invalid decode
            if s[i] == '0':
                return 0
            
            if i in memo:
                return memo[i]

            # single digit choice
            single_digit = helper(i + 1)

            # double digit choice
            double_digit = 0
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                double_digit = helper(i + 2)

            memo[i] = single_digit + double_digit
            return memo[i]

        return helper(0)
