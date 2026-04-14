class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sqr_map = {}
        row_map = {}
        column_map = {}
        for i in range(9):
            sqr_map[i] = set()
            row_map[i] = set()
            column_map[i] = set()

        for row in range(len(board)):
            for column in range(len(board[row])):
                sqrIndex = ((row // 3) * 3) + (column // 3)
                num = board[row][column]
                if num == ".":
                    continue
                if num in column_map[column] or num in row_map[row] or num in sqr_map[sqrIndex]:
                    return False
                sqr_map[sqrIndex].add(num) 
                row_map[row].add(num)
                column_map[column].add(num)
        return True
                        