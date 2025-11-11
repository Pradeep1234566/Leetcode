class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        N = len(nums)

        for j in range(N):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]



        return i + 1
