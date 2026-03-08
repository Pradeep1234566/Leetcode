from collections import deque
class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        queue = deque(range(1, n+1))

        while len(queue) > 1:

            for _ in range(k-1):
                queue.append(queue.popleft())
    
            queue.popleft()
        
        return queue[0]

        