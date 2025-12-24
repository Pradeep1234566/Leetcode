class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 or n % 2 == 0 :
            return False
        
        while n>1:
            remainder = n % 3
            if remainder != 0:
                return False
            
            n = n // 3
        
        return True
        