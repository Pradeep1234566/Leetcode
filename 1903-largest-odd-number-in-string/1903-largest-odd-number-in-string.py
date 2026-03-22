class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num)
        temp = num[n-1]

        if int(temp) % 2 != 0:
            return num
        
        for i in range(n-1, -1, -1):
            temp = int(num[i])
            if temp % 2 != 0:
                return num[:i+1]
        
        return ''