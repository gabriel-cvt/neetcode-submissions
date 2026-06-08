class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    
        memo = {}
        def dp(index, current):
            if (index, current) in memo:
                return memo[(index, current)]

            if index == len(nums):
                return 1 if current == target else 0
            
            add = dp(index + 1, current + nums[index])
            sub = dp(index + 1, current - nums[index])

            memo[(index, current)] = add + sub
            return add + sub
        return dp(0, 0)
            