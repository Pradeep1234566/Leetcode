from collections import deque

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        outdegree = [0] * n
        reversed_graph = [[] for _ in range(n)]

        # Build reversed graph and outdegree count
        for i in range(n):
            for adjacent in graph[i]:
                reversed_graph[adjacent].append(i)
                outdegree[i] += 1

        queue = deque()
        for i in range(n):
            if outdegree[i] == 0:  # terminal nodes
                queue.append(i)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbour in reversed_graph[node]:
                outdegree[neighbour] -= 1
                if outdegree[neighbour] == 0:
                    queue.append(neighbour)

        return sorted(result)
