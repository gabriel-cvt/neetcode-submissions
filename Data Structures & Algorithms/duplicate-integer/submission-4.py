class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}

        for x in nums:
            if x in numMap.keys():
                return True
            numMap[x] = 1
        return False
        