class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def dp(index):
            if index in memo:
                return memo[index]
            
            if index >= n:
                return 0

            memo[index] = max(nums[index] + dp(index + 2), dp(index + 1))
            return memo[index]

        return dp(0)