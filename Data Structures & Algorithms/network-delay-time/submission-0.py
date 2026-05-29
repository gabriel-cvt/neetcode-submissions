from collections import deque
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adList = {}
        for source, target, time in times:
            if source not in adList:
                adList[source] = []
            adList[source].append((target, time))

        distance = {
            k:0
        }
        heap = [(0, k)]
        while heap:
            currDist, node = heapq.heappop(heap)
            if currDist > distance[node]:
                continue
            for target, time in adList.get(node, []):
                newDist = currDist + time
                if newDist < distance.get(target, float('inf')):
                    distance[target] = newDist
                    heapq.heappush(heap, (newDist, target))

        return max(distance.values()) if len(distance) == n else -1