class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            if row < 0 or row > m -1 or col < 0 or col > n -1:
                return 0
            if row == m -1 and col == n -1:
                return 1
            
            res = dp(row + 1, col) + dp(row, col + 1)
            memo[(row, col)] = res
            return res
        return dp(0, 0)