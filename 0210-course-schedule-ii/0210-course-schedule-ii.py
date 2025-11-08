from collections import deque

class Solution(object):
    def bfs(self, queue, adj, indegree, result):
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbours in adj[node]:
                indegree[neighbours] -= 1
                if indegree[neighbours] == 0:
                    queue.append(neighbours)
        return result

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(numCourses)]

        for course, precourse in prerequisites:
            adj[precourse].append(course)
        
        indegree = [0] * numCourses

        for i in range(numCourses):
            for adjacent in adj[i]:
                indegree[adjacent] += 1
        

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append((i))
        
        result = []
        result = self.bfs(queue, adj, indegree, result)
        
        if len(result) == numCourses:
            return result
        
        return []
