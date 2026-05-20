class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        n = len(cost) -1
        def helper(i):
            if i in memo:
                return memo[i]
            
            if i <= 1:
                result = cost[i]
            else:
                result = cost[i] + min(helper(i - 1), helper(i - 2))
            memo[i] = result
            return result

        return min(helper(n), helper(n -1))
