class Solution(object):
    def sortedSquares(self, nums):
        results = []
        left = 0
        right = len(nums) - 1
        while left<=right:
            if nums[right]**2 > nums[left] ** 2:
                results.append(nums[right] ** 2)
                right -= 1
            else:
                results.append(nums[left] ** 2)
                left += 1

        
        results.reverse()

        return results
