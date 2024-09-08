class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = []
        if n < 0:
            return False
        if n == 0:
            return False
        if n == 1:
            return True
        else:
            while n:
                k = n % 2
                n = n // 2
                binary.append(k)
            count = 0
            for i in binary:
                if i == 1:
                    count += 1
                    if count > 1:
                        return False
            return True
    

        