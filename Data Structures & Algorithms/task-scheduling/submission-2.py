import heapq
from collections import deque, Counter

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:        
        count = Counter(tasks)
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count < 0:
                    q.append((time + n, count))

            while q and q[0][0] <= time:
                _, count = q.popleft()
                heapq.heappush(heap, count)
        
        return time

        

        