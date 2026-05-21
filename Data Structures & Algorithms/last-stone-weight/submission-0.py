import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            newW = abs(x - y)
            if newW != 0:
                heapq.heappush(stones, -newW)
        
        if len(stones) == 1:
            return -stones[0]
        return 0
