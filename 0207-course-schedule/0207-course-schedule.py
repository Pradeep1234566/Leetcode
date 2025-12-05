from collections import deque

class Solution(object):
    def bfs(self, queue, indegree, count, adjacency_list):
        while queue:
            node = queue.popleft()
            count += 1     # FIXED: count when processing node

            for neighbours in adjacency_list[node]:
                indegree[neighbours] -= 1
                if indegree[neighbours] == 0:
                    queue.append(neighbours)
        
        return count

        
    def canFinish(self, numCourses, prerequisites):
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()

        # Build graph
        for course, precourse in prerequisites:
            adj_list[precourse].append(course)
            indegree[course] += 1
        
        # Push all nodes with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # Start count at 0 (FIXED)
        count = 0

        # BFS
        processed = self.bfs(queue, indegree, count, adj_list)

        # If topo length == numCourses → no cycle
        return processed == numCourses
