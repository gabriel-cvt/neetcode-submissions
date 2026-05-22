class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = currMax = currMin = nums[0]
        for num in nums[1:]:
            tempMax = max(num, currMax * num, currMin * num)
            currMin = min(num, currMax * num, currMin * num)
            currMax = tempMax
            result = max(currMax, result)
        return result