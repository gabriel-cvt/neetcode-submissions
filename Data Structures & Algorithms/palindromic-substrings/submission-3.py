class Solution:
    def countSubstrings(self, s: str) -> int:

        memo = {}
        def dp(left, right):
            if (left, right) in memo:
                return memo[left, right]

            isPal = False
            if (left >= right) or (s[left] == s[right] and dp(left + 1, right -1)):
                isPal = True
            memo[(left, right)] = isPal
            return isPal
        
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp(i, j):
                    count += 1
        return count
        
