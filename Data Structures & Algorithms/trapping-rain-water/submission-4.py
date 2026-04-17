class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        lmax = height[l]
        rmax = height[r]
        result = 0
        while l < r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                result += lmax - height[l]
                l += 1
            else:
                rmax= max(rmax, height[r])
                result += rmax - height[r]
                r -= 1
        return result 