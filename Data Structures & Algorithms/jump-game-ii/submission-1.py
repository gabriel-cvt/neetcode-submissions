class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums) -1
        def dp(index):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]

            result = float('inf')
            for i in range(nums[index], 0, -1):
                result = min(result, dp(index + i) + 1)
            memo[index] = result
            return result
        return dp(0)