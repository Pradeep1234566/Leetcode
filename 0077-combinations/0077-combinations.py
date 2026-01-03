class Solution(object):
    def helper(self, start, n, k, temp, result):
       
        if len(temp) == k:
            result.append(temp[:])
            return
        
        for num in range(start, n + 1):
            temp.append(num)
            self.helper(num + 1, n, k, temp, result)
            temp.pop()  # backtrack

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(1, n, k, [], result)
        return result
