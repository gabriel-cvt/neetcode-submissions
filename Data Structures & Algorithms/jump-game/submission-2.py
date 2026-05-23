class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        n = len(nums) -1
        def dp(index):
            if index >= n:
                return True
            if index in memo:
                return memo[index]
        
            result = False
            if nums[index] == 0:
                memo[index] = result
                return result
            
            for i in range(nums[index], 0, -1):
                if dp(index + i):
                    result = True
                    break

            memo[index] = result
            return result
        return dp(0)

