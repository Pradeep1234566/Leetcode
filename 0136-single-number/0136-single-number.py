class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0

        for i in nums:
            xor = xor ^ i

        return xor