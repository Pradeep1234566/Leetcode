class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        N = len(height)

        left = 0
        right = N - 1

        while left < right:
            width = right - left

            water_level = (width) * min(height[left], height[right])

            max_water = max(max_water, water_level)


            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
            
        
        return max_water
        