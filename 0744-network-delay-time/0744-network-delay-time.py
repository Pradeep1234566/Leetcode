import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 1-indexed distance array
        distance = [float('inf')] * (n + 1)
        distance[k] = 0

        heap = [(0, k)]  # (time, node)

        while heap:
            time, node = heapq.heappop(heap)
            # Skip if we already found a better route
            if time > distance[node]:
                continue

            for neighbour, weight in graph[node]:
                if distance[neighbour] > time + weight:
                    distance[neighbour] = time + weight
                    heapq.heappush(heap, (time + weight, neighbour))

        max_time = max(distance[1:])
        return max_time if max_time < float('inf') else -1
