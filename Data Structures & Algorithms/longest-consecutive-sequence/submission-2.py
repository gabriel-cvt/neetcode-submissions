class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)

        result = 0
        size = 1
        current = 0
        for num in hashset:
            if num -1 not in hashset:
                current = num
                size = 1;
            while current+1 in hashset:
                current = current +1
                size = size + 1
            result = max(size, result)

        return result