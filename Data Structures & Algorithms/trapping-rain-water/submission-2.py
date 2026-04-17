class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        lmax = l
        rmax = r
        result = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= height[lmax]:
                    lmax = l
                result += height[lmax] - height[l]
                l += 1
            else:
                if height[r] >= height[rmax]:
                    rmax = r
                result += height[rmax] - height[r]
                r -= 1
        return result 