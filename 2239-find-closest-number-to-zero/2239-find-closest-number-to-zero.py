class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for i in nums:
            if abs(closest) > abs(i) or (abs(closest) == abs(i) and i > closest):
                closest = i
        return closest
