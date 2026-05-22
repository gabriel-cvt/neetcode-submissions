class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

        def dp(currSum, i):
            if i == len(nums):
                return False
            if currSum + nums[i] == totalSum / 2:
                return True
            if dp(currSum + nums[i], i + 1):
                return True
            return dp(currSum, i + 1)
        
        return dp(0, 0)
            

