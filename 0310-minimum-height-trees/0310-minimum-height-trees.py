class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]  # edge case: single node

        adj_list = [[] for _ in range(n)]
        degree = [0] * n

        for u, w in edges:
            adj_list[u].append(w)
            adj_list[w].append(u)
            degree[u] += 1
            degree[w] += 1

        leaves = []
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        remaining = n  # track how many nodes are still alive

        while remaining > 2:  # stop when 1 or 2 nodes left
            next_leaves = []
            remaining -= len(leaves)  # remove this round's leaves

            for leaf in leaves:
                for neighbour in adj_list[leaf]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        next_leaves.append(neighbour)

            leaves = next_leaves  # move to next round

        return leaves