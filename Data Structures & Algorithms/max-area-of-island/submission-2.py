class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row, column):    
            grid[row][column] = 0
            area = 1
            # Horizontal
            if column > 0 and grid[row][column -1] == 1:
                area += dfs(row, column - 1)
            
            if column < len(grid[row]) -1 and grid[row][column + 1] == 1:
                area += dfs(row, column + 1)

            # Vertical
            if row > 0 and grid[row -1][column] == 1:
                area += dfs(row - 1, column)
            if row < len(grid)-1 and grid[row + 1][column] == 1:
                area += dfs(row + 1, column)

            return area
        max_count = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    curr = dfs(row, column)
                    max_count = max(max_count, curr)
        return max_count