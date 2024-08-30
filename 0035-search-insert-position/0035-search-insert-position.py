class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = left + (right - left)//2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid + 1
            else:
                right = mid - 1
        if left>=right:
            return mid+1
        elif right<0:
            return mid - 1