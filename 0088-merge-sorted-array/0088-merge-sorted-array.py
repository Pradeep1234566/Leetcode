class Solution(object):
    def merge(self, nums1, m, nums2, n):

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # m = len(nums1)
        # n = len(nums2)
        i = m + n -1 
        j = n - 1
        if j == 0:
            nums1[i] = nums2[0]
        else:
            while i>=m:
                nums1[i] = nums2[i-j-1]
                i -= 1
        nums1.sort()
