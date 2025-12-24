import math

class Solution(object):
    def getPermutation(self, n, k):
        numbers = []
        result = []

        for i in range(1, n + 1):
            numbers.append(str(i))   # convert to string early

        for i in range(n, 0, -1):
            ways = math.factorial(i - 1)   # FIX 1
            block = (k - 1) // ways

            result.append(numbers.pop(block))
            k = (k - 1) % ways + 1          # FIX 2

        return "".join(result)              # FIX 3
