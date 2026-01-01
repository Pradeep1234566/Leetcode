class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = 0
        n = len(digits)

        for i in range(n):
            digit = digit + (digits[n-i-1]*(10**(i)))
        
        
        digit += 1
        result = []

        while digit:
            temp = digit % 10
            result.append(temp)
            digit = digit // 10
        
        return result[::-1]