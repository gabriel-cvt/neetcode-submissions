import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = nums[:]
        heapq.heapify(self.heap)
        self.fixHeapSize()
    
    def fixHeapSize(self):
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.fixHeapSize()
        return self.heap[0]

        
