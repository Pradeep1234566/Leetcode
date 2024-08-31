class Solution(object):
    def isPerfectSquare(self, num):
        k = 0
        i = 1
        while k<=num:
            k = i * i
            i += 1
            if k == num:
                return True
        return False

        