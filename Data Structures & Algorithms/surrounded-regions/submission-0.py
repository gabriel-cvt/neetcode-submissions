class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(row, col, seen):
            seen.add((row, col))

            for rInc, cInc in directions:
                newR = row + rInc
                newC = col + cInc
                if (0 <= newR < rows and
                    0 <= newC < cols and
                    (newR, newC) not in seen and
                    board[newR][newC] == "O"
                    ): dfs(newR, newC, seen)
        
        left = [(r, 0) for r in range(rows) if board[r][0] == "O"]
        right = [(r, cols -1) for r in range(rows) if board[r][cols-1] == "O"]
        upper = [(0, c) for c in range(cols) if board[0][c] == "O"]
        bottom = [(rows-1, c) for c in range(cols) if board[rows-1][c] == "O"]
        starters = left + right + upper + bottom
        seen = set()
        for r, c in starters:
            dfs(r, c, seen)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in seen:
                    board[r][c] = "X"
