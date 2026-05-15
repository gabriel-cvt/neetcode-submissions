class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(row, col, seen):
            seen.add((row, col))

            for rInc, cInc in [(-1,0), (0,-1), (0,1), (1,0)]:
                newR = row + rInc
                newC = col + cInc
                if ((newR, newC) not in seen and
                    0 <= newR < rows and
                    0 <= newC < cols and
                    heights[newR][newC] >= heights[row][col]
                ):
                    dfs(newR, newC, seen)

        pacificSeen, atlanticSeen = set(), set()

        for r in range(rows):
            dfs(r, 0, pacificSeen)
        for c in range(cols):
            dfs(0, c, pacificSeen)
        for r in range(rows):
            dfs(r, cols -1, atlanticSeen)
        for c in range(cols):
            dfs(rows -1, c, atlanticSeen)

        return list(atlanticSeen & pacificSeen)
