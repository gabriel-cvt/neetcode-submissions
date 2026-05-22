class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(prev, curr):
            if curr == len(nums):
                return 0
            
            if (prev, curr) in memo:
                return memo[(prev, curr)]

            if prev == -1 or nums[curr] > nums[prev]:
                result = max(
                    1 + dp(curr, curr + 1),
                    dp(prev, curr + 1)
                )
            else:
                result = dp(prev, curr +1)
            memo[(prev, curr)] = result
            return result

        return dp(-1, 0)
