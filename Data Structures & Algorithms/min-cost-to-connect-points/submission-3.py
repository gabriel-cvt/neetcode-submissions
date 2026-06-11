import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = {i: [] for i in range(n)}
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cost = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append([cost, j])
                adj[j].append([cost, i])
        
        heap = [[0, 0]]
        res = 0
        visited = set()
        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if not nei in visited:
                    heapq.heappush(heap, [neiCost, nei])
        return res


