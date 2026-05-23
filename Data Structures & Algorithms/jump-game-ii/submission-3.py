class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        longest = 0
        for i in range(len(nums) -1):
            longest = max(longest, nums[i] + i)

            if i == current_end:
                jumps += 1
                current_end = longest
        return jumps