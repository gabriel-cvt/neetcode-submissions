
# Encontra o primeiro 1
# Aplica o algorítmo de DFS nele, percorrendo pelos vizinhos
# Ao encontrar um vizinho que também é um, aplica DFS nele e marca como 0

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(row, column):
            # Marcar como 0
            grid[row][column] = '0'

            # Horizontal
            if column > 0 and grid[row][column -1] == '1':
                dfs(row, column - 1)
            
            if column < len(grid[row]) -1 and grid[row][column + 1] == '1':
                dfs(row, column + 1)

            # Vertical
            if row > 0 and grid[row -1][column] == '1':
                dfs(row - 1, column)
            if row < len(grid)-1 and grid[row + 1][column] == '1':
                dfs(row + 1, column)

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == '1':
                    count += 1
                    dfs(row, column)

        return count