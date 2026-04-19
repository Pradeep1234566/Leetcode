class Solution(object):
    def helper(self, adj_list, visited, node):
        visited.add(node)
        for neighbours in adj_list[node]:
            if neighbours not in visited:
                self.helper(adj_list, visited, neighbours)
        
    
    def findCircleNum(self, isConnected):
        V = len(isConnected)
        
        adj_list = [[] for _ in range(V)]
        
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        

        visited = set()
        count = 0

        for i in range(V):
            if i not in visited:
                self.helper(adj_list, visited, i)
                count += 1
    
        return count

        