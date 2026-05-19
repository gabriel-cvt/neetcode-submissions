class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            
            if n == 1:
                result = 1
            elif n == 2:
                result = 2
            else:
                result = helper(n - 1) + helper(n -2)
            
            memo[n] = result
            return result
        return helper(n)

                
