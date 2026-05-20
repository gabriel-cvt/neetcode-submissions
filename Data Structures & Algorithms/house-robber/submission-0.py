class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max(nums[0], nums[1])

        memo = {}

        def dp(index):
            if index in memo:
                return memo[index]
            
            if index >= len(nums):
                return 0

            if index == len(nums) -1:
                result = nums[index]
            else:
                result = max(nums[index] + dp(index + 2), dp(index + 1))
            memo[index] = result
            return result

        return dp(0)