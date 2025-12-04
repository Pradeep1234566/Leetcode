class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i in nums:
            if count == 0:
                number = i
                count += 1
            elif count != 0:
                if number == i:
                    count += 1
                else:
                    count -= 1
        
        return number
        