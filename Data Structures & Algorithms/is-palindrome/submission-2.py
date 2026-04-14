class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = ''.join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(normalized) -1
        while left <= right:
            if normalized[left] != normalized[right]:
                return False
            left += 1
            right -= 1
        return True
            