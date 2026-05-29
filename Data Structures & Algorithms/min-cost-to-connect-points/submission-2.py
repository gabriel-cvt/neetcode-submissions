import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        heap = []
        for i in range(len(points) -1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x2 - x1) + abs(y2 - y1)
                heapq.heappush(heap, (cost, i, j))
        
        res = 0
        n = 0
        parent = [i for i in range(len(points))]
        while n < len(points) -1:
            cost, a, b = heapq.heappop(heap)
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                continue

            parent[rootA] = rootB
            res += cost
            n += 1
        return res


