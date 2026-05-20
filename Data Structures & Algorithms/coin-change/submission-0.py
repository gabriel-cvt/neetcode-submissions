class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(a, b):
            if a is None:
                return b
            if b is None:
                return a
            return min(a, b)
        memo = {}
        def dp(amount):
            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0
            else:
                result = None
                for coin in coins:
                    sub = amount - coin
                    if sub < 0:
                        continue
                    sub_result = dp(sub)
                    if sub_result is None:
                        continue
                    result = helper(result, dp(sub) + 1)

                memo[amount] = result
                return result

        result = dp(amount)

        return result if result is not None else -1
