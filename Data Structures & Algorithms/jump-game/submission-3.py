class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i <= maxReach and i + nums[i] >= maxReach:
                maxReach = i + nums[i]
        return maxReach >= len(nums) -1