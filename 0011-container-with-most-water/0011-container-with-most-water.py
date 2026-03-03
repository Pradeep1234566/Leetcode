class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        max_area = 0
        left_index = 0
        right_index = N - 1

        while left_index <= right_index:
            ht = min(height[left_index], height[right_index])
            width = right_index - left_index
            area = ht * width 
            max_area = max(max_area, area)

            if height[left_index] > height[right_index]:
                right_index -= 1
            
            else:
                left_index += 1
        
        return max_area
