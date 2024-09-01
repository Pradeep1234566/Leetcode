class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = []
        a = len(nums) - k
        if k == 0 or k > len(nums):
           pass
        else:
            for i in range(a, len(nums)):
                temp.append(nums[i])

            for i in range(0, a+1):
                temp.append(nums[i])
            print(temp)

            k = len(temp)
            print(k)
            m = len(nums)
            print(m)
            for i in range(m):
                nums[i] = temp[i]
