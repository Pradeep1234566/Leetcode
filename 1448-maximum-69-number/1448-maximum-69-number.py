class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = []

        while num:
            digits.append(num%10)
            num = num / 10
        track = 1
        digits.reverse()
        
        for idx in range(len(digits)):
            if digits[idx] == 6 and track == 1:
                digits[idx] = 9
                track = 0 
            
            
        N = len(digits)
        result = 0

        for i in range(N):
            result = result + digits[i] * (10 ** (N-i-1))
        
        return result
        


        