class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        sorted_map = sorted(hashmap.items(), key=lambda x : x[1], reverse=True)
        return [x[0] for x in sorted_map[:k]]
            
