class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = 0
        a = num
        while a:
            s += a%10
            a = a /10
            k = s
            if a == 0:
                if k >=10:
                    a = k
                    s = 0
        return s
            
