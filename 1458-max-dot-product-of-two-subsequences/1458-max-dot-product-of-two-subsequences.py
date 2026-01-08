class Solution(object):
    def helper(self, nums1, nums2, index1, index2, n, m, dp):
        if index1 == n or index2 == m:
            return float('-inf')
        
        if dp[index1][index2] is not None:
            return dp[index1][index2]
        
        product = nums1[index1] * nums2[index2]

        dp[index1][index2] =  max(
            product,
            product + self.helper(nums1, nums2, index1 + 1, index2 + 1, n, m, dp),
            self.helper(nums1, nums2, index1 + 1, index2, n, m, dp),
            self.helper(nums1, nums2, index1, index2 + 1, n, m, dp)
        )
        
        return dp[index1][index2]

    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        dp = [[None]*m for _ in range(n)]
        return self.helper(nums1, nums2, 0, 0, n, m, dp)
        