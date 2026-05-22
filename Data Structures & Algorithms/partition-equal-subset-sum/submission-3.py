class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        target = totalSum // 2
        if totalSum % 2 != 0:
            return False

        memo = {}
        def dp(currSum, i):
            
            if currSum == target:
                return True

            if currSum in memo:
                return memo[currSum]

            if i == len(nums) or currSum > target:
                return False
            

            memo[currSum] = dp(currSum + nums[i], i + 1) or dp(currSum, i + 1)
            return memo[currSum]
        
        return dp(0, 0)
            

