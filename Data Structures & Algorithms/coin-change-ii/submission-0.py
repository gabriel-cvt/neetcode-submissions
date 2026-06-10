class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dp(i, remaining):
            if (i, remaining) in cache:
                return cache[(i, remaining)]
            
            if remaining == 0:
                return 1
            
            if remaining < 0:
                return 0
            
            if i == len(coins):
                return 0
            
            take = dp(i, remaining - coins[i])
            skip = dp(i + 1, remaining)
            cache[(i, remaining)] = take + skip
            return take + skip
        return dp(0, amount)