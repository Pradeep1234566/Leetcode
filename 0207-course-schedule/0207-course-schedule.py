from collections import deque

class Solution(object):
    def bfs(self, queue, indegree, count, adjacency_list):
        while queue:
            node = queue.popleft()
            count += 1

            for neighbour in adjacency_list[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return count

    def canFinish(self, numCourses, prerequisites):
        adjacency_list = [[] for _ in range(numCourses)]

        # Build adjacency list (directed graph)
        for course, precourse in prerequisites:
            adjacency_list[precourse].append(course)
        
        # Compute indegree
        indegree = [0] * numCourses
        for i in range(numCourses):
            for neighbour in adjacency_list[i]:
                indegree[neighbour] += 1
        
        # Queue for all nodes with indegree 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        count = self.bfs(queue, indegree, count, adjacency_list)

        # If we processed all courses, return True
        return count == numCourses
