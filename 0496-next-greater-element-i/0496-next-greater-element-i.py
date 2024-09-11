class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in nums1:
            # Find the index of i in nums2
            idx = nums2.index(i)
            key = 0
            # Look for the next greater element to the right of the index
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > i:
                    key = 1
                    answer.append(nums2[j])
                    break
            if key == 0:
                answer.append(-1)
        
        return answer