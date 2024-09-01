class Solution(object):
    def rearrangeArray(self, nums):
        """
        Rearrange the array so that every consecutive pair has opposite signs.
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = []
        negative = []
        
        # Separate positive and negative numbers
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        
        # Merge the lists alternately
        result = []
        for pos, neg in zip(positive, negative):
            result.append(pos)
            result.append(neg)
        
        return result
