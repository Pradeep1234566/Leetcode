class Solution(object):
    def singleNumber(self, nums):
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
        print(freq)
        for key, item in freq.items():
            if item == 1:
                return key
        