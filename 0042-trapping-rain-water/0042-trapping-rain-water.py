class Solution:
    def trap(self, height):
        N = len(height)
        left_max = [0] * N
        right_max = [0] * N
        water = 0
    

        left_max[0] = height[0]
        for i in range(1, N):
            left_max[i] = max(left_max[i-1], height[i])
        
        right_max[N-1] = height[N-1]
        for i in range(N-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        

        for i in range(N):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water



        