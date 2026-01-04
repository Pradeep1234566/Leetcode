class Solution(object):
    def helper(self, n):
        divisors = []

        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1

        if len(divisors) == 4:
            return sum(divisors)
        return 0

    def sumFourDivisors(self, nums):
        total = 0
        for x in nums:
            total += self.helper(x)
        return total
