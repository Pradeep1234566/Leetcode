class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        k = len(nums) // 3
        # print(freq)
        result = []
        for items, key in freq.items():
            if key> k:
                result.append(items)
        
        return result
