class Solution(object):
    def helper(self, left, right, memo):
        if left > right:
            return 1
        
        if (left, right) in memo:
            return memo[(left, right)]

        total = 0

        for i in range(left, right+1):
            left_subtrees = self.helper(left, i-1, memo)
            right_subtrees = self.helper(i+1, right, memo)

            total += (left_subtrees*right_subtrees)
        
        memo[(left, right)] = total
        return total
        

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        memo = {}
        return self.helper(left, right, memo)

        