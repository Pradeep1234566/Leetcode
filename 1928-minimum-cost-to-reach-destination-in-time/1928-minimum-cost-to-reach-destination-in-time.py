import heapq

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        graph = [[] for _ in range(n)]

        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Track minimum time to reach each node
        best_time = [float('inf')] * n
        best_time[0] = 0

        # Min-heap by cost
        pq = [(passingFees[0], 0, 0)]  # (cost, time, node)

        while pq:
            cost, time, node = heapq.heappop(pq)

            if node == n - 1:
                return cost

            for nei, t in graph[node]:
                newTime = time + t
                newCost = cost + passingFees[nei]

                if newTime > maxTime:
                    continue

                # Only explore if this is a faster way to reach 'nei'
                if newTime < best_time[nei]:
                    best_time[nei] = newTime
                    heapq.heappush(pq, (newCost, newTime, nei))

        return -1
