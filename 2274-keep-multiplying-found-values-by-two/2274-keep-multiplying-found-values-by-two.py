class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        temp = set(nums)

        if original in temp:
            while original in temp:
                original = 2 * original

            return original
            
        else:
            return original
        