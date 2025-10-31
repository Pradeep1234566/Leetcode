class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}

        # count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # collect the two numbers that appear twice
        sneaky = []
        for num, cnt in freq.items():
            if cnt == 2:
                sneaky.append(num)

        # the problem guarantees exactly two such numbers
        return sneaky