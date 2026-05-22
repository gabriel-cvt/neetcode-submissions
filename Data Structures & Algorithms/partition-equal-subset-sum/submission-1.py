class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        target = totalSum // 2
        if totalSum % 2 != 0:
            return False

        memo = {}
        def dp(currSum, i):
            if i == len(nums) or currSum > target:
                return False
            if (currSum, i) in memo:
                return memo[(currSum, i)]
            
            cond = False
            if currSum == target:
                cond = True
            if dp(currSum + nums[i], i + 1) or dp(currSum, i + 1):
                cond = True
            memo[(currSum, i)] = cond
            return cond
        
        return dp(0, 0)
            

