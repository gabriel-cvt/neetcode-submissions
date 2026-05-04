class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def dfs(row, col, k):
            if k == len(word):
                return True
            
            if row < 0 or row >= len(board):
                return False
            if col < 0 or col >= len(board[row]):
                return False

            if (row, col) in visited:
                return False

            if board[row][col] != word[k]:
                return False

            visited.add((row, col))
            if (dfs(row, col - 1, k + 1) or
                dfs(row, col + 1, k + 1) or
                dfs(row - 1, col, k + 1) or
                dfs(row  +1, col, k + 1)):
                visited.remove((row, col))
                return True

            visited.remove((row, col))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
        
        