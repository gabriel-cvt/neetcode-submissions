class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resLeft = resRight = 0
        def expand(left, right):
            nonlocal resLeft, resRight
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            if right - left > resRight - resLeft:
                resRight = right
                resLeft = left +1

        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return s[resLeft:resRight]