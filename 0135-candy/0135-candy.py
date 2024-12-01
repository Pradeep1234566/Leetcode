class Solution(object):
    def candy(self, ratings):
        N = len(ratings)
        left_array = [1] * N
        right_array = [1] * N
        
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left_array[i] = left_array[i - 1] + 1
        
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_array[i] = right_array[i + 1] + 1
        
        for i in range(N):
            left_array[i] = max(left_array[i], right_array[i])
        
        return sum(left_array)
