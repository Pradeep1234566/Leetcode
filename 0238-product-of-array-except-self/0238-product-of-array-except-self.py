class Solution(object):
    def productExceptSelf(self, nums):
        answer = [] 
        n = len(nums)
        l = 1
        r = 1
        left =  [0] * n
        right = [0] * n
        for i in range(n):
            j = n - i - 1
            left[i] = l
            right[j] = r
            l *= nums[i]
            r *= nums[j]
        return [l*r for l, r in zip(left, right)]            
        