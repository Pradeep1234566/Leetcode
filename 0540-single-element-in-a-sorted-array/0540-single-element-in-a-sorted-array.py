class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for number, times in freq.items():
            if times == 1:
                return number
        