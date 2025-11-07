from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        N = len(graph)
        color = [-1] * N

        for i in range(N):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0

            while queue:
                node = queue.popleft()
                for neighbours in graph[node]:
                    if color[neighbours] == -1:
                        color[neighbours] = 1 - color[node]
                        queue.append((neighbours))
                    elif color[neighbours] == color[node]:
                        return False

        return True

        
        