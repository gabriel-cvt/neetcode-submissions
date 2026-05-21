import heapq
from collections import deque, Counter

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:        
        aux = [0] * 26
        for letter in tasks:
            aux[ord(letter) - ord('A')] -= 1
        heap = []

        for task in aux:
            if task < 0:
                heapq.heappush(heap, task)
        heapq.heapify(heap)
        
        q = deque()
        time = 0
        while heap or q:
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count < 0:
                    q.append((time + n + 1, count))
            time += 1
            while q and q[0][0] <= time:
                avl_time, count = q.popleft()
                heapq.heappush(heap, count)
        
        return time

        

        