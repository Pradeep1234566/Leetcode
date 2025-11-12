import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))
        
        heap = [(0, src, 0)]  # (stops, city, cost)
        dist = [float('inf')] * n
        dist[src] = 0

        while heap:
            stop, city, cost = heapq.heappop(heap)

            if stop > k:
                continue
            
            for next_city, price in graph[city]:
                if dist[next_city] > cost + price and stop <= k:
                    dist[next_city] = cost + price
                    heapq.heappush(heap, (stop + 1, next_city, cost+price))
            
        if dist[dst] == float('inf'):
            return -1
        
        return dist[dst]

        