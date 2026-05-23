class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        n = len(nums) -1
        def dp(index):
            if index == n:
                return True
            if index in memo:
                return memo[index]
        
            if index >= n or nums[index] == 0:
                memo[index] = False
                return False
            
            for i in range(nums[index], 0, -1):
                if dp(index + i):
                    memo[index] = True
                    return True
            memo[index] = False
            return False
        return dp(0)

