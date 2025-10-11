class Solution(object):
    def helper(self, start, k, n, arr, result, temp, N):
        if len(temp) == k:
            if n == 0:
                result.append(list(temp))
            return
        
        for i in range(start, N):
            if arr[i] > n:  # pruning
                break
            temp.append(arr[i])
            self.helper(i + 1, k, n - arr[i], arr, result, temp, N)
            temp.pop()

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        self.helper(0, k, n, arr, result, [], len(arr))
        return result
