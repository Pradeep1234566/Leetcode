class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        next_largest = 0
        maxi = float('inf')
        
        break_index = -1  # ✅ initialize

        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                break_point = nums[i-1]
                break_index = i - 1 
                break
        
    
        if break_index == -1:
            nums.reverse()
            return

        for i in range(n-1, break_index, -1):
            difference = nums[i] - break_point
            if difference > 0 and difference < maxi: 
                maxi = difference 
                next_largest = nums[i]
                next_largest_index = i

        nums[break_index], nums[next_largest_index] = nums[next_largest_index], nums[break_index]

        nums[break_index+1:] = nums[break_index+1:][::-1]