class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    
        def dp(index, current):
            if index == len(nums):
                return 1 if current == target else 0
            
            add = current + nums[index]
            sub = current - nums[index]
            return dp(index + 1, add) + dp(index +1, sub)
        return dp(0, 0)
            