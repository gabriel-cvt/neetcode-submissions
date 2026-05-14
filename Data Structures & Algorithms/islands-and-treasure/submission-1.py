from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))

        while q:
            row, col = q.popleft()
            
            if row > 0 and (row -1, col) not in seen:
                if grid[row-1][col] != -1:
                    q.append((row-1, col))
                    seen.add((row-1, col))
                    grid[row-1][col] = grid[row][col] + 1

            if row < len(grid) -1 and (row + 1, col) not in seen:
                if grid[row+1][col] != -1:
                    q.append((row+1, col))
                    seen.add((row+1, col))
                    grid[row+1][col] = grid[row][col] + 1

            if col < len(grid[row]) -1 and (row, col +1) not in seen:
                if grid[row][col +1] != -1:
                    q.append((row, col +1))
                    seen.add((row, col +1))
                    grid[row][col +1] = grid[row][col] + 1
            
            if col > 0 and (row, col -1) not in seen:
                if grid[row][col -1] != -1:
                    q.append((row, col -1))
                    seen.add((row, col -1))
                    grid[row][col -1] = grid[row][col] + 1
                
