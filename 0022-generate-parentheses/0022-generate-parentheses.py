class Solution(object):
    def helper(self, curr, result, open, close, n):
        if len(curr) == 2 * n:
            result.append(curr)
            return 
        
        if open < n:
            self.helper(curr + '(', result, open + 1, close, n)
        
        if close < open:
            self.helper(curr + ')', result, open, close + 1, n)

        

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        open = 0
        close = 0
        
        self.helper('', result, open, close, n)

        return result