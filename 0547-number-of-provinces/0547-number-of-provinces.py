class Solution(object):
    def dfs(self, node, visited, adjacency_list):
        visited[node] = 1
        for val in adjacency_list[node]:
            if visited[val] != 1:
                self.dfs(val, visited, adjacency_list)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        adjacency_list = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)
        
        visited = [0] * n
        count = 0
        for i in range(n):
            if visited[i] != 1:
                self.dfs(i, visited, adjacency_list)
                count += 1
        return count
