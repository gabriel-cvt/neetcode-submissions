class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, HashSet<Character>> rows = new HashMap<>();
        HashMap<Integer, HashSet<Character>> columns = new HashMap<>();
        HashMap<Integer, HashSet<Character>> squares = new HashMap<>();
        
        for (int i = 0; i < 9; i++) {
            rows.put(i, new HashSet<>());
            columns.put(i, new HashSet<>());
            squares.put(i, new HashSet<>());
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                int sqrIndex = ((i / 3) * 3) + (j / 3);
                if (board[i][j] == '.') {
                    continue;
                }
                if (rows.get(i).contains(board[i][j]) ||
                    columns.get(j).contains(board[i][j]) ||
                    squares.get(sqrIndex).contains(board[i][j])) {
                        return false;
                    }
                    rows.get(i).add(board[i][j]);
                    columns.get(j).add(board[i][j]);
                    squares.get(sqrIndex).add(board[i][j]);
            }    
        }
        return true;
    }
}
