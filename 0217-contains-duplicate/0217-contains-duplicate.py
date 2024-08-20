class Solution(object):
    def containsDuplicate(self, nums):
        k = set(nums)
        if len(k) < len(nums):
            return True
        else:
            return False
        