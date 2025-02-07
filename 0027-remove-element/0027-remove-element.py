class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Pointer for the new array position
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move the non-val element forward
                k += 1
        return k  # Number of elements not equal to val
