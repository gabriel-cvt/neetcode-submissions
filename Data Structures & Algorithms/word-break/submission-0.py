class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                memo[i] = True
                return True
            
            result = False
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in wordDict:
                    if dp(j):
                        result = True
            memo[i] = result
            return result

        return dp(0)