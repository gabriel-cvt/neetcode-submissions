# condições para retornar -1
# 1. não ter frutas podres
# 2. as frutas podres não chegarem em todas as frutas normais


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        seen = set()
        fruits = set()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fruits.add((r,c))
                elif grid[r][c] == 2:
                    q.append((r, c))
                    seen.add((r, c))
                    fruits.add((r, c))
        
        if fruits == seen:
            return 0

        result = 0

        while q:

            for _ in range(len(q)):
                r, c = q.popleft()
                if r > 0 and grid[r-1][c] == 1 and (r-1, c) not in seen:
                    q.append((r-1, c))
                    seen.add((r-1, c))
                if r < len(grid) -1 and grid[r+1][c] == 1 and (r+1, c) not in seen:
                    q.append((r+1, c))
                    seen.add((r+1, c))
                if c > 0 and grid[r][c -1] == 1 and (r, c-1) not in seen:
                    q.append((r, c -1))
                    seen.add((r, c -1))
                if c < len(grid[r]) -1 and grid[r][c +1] == 1 and (r, c+1) not in seen:
                    q.append((r, c+1))
                    seen.add((r, c+1))
            if q:
                result += 1

        return result if fruits == seen else -1

