class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxwater = 0
        N = len(height)
        left = 0
        right = N - 1

        while left < right:

            width = right - left 

            volume = width * (min(height[left], height[right]))

            maxwater = max(maxwater, volume)

            if height[left] > height[right]:
                right -= 1
            
            else:
                left += 1
        
        return maxwater
        