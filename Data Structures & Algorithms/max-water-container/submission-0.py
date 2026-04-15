class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1

        result = 0
        while l < r:
            x = r - l
            y = min(heights[l], heights[r])
            mul = x * y
            if mul > result:
                result = mul
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result
