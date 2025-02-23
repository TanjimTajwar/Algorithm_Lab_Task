import java.util.*;

class NQueens {
    public static void main(String[] args) {
        try (Scanner Arnab = new Scanner(System.in)) { // Try-with-resources
            System.out.print("Enter the number of Queens: ");
            int n = Arnab.nextInt();

            List<List<String>> mylist = findNQueen(n);

            System.out.println("The pattern for " + n + " Queen problem is:");

            for (List<String> board : mylist) {
                for (String row : board) {
                    System.out.println(row);
                }
                System.out.println();
            }
        } // Scanner automatically closed here
    }

    public static List<List<String>> findNQueen(int n) {
        List<List<String>> allBoards = new ArrayList<>();
        char[][] board = new char[n][n];

        // Initialize board with '.'
        for (int i = 0; i < n; i++) {
            Arrays.fill(board[i], '.');
        }

        helper(board, allBoards, 0);
        return allBoards;
    }

    public static void helper(char[][] board, List<List<String>> allBoards, int col) {
        if (col == board.length) {
            saveBoard(allBoards, board);
            return;
        }

        for (int a = 0; a < board.length; a++) {
            if (isSafe(a, col, board)) {
                board[a][col] = 'Q'; // Place queen
                helper(board, allBoards, col + 1); // Recursive call
                board[a][col] = '.'; // Backtrack
            }
        }
    }

    public static boolean isSafe(int row, int col, char[][] board) {
        // Check left side of row
        for (int a = 0; a < col; a++) {
            if (board[row][a] == 'Q') {
                return false;
            }
        }

        // Check upper diagonal (left)
        for (int a = row, b = col; a >= 0 && b >= 0; a--, b--) {
            if (board[a][b] == 'Q') {
                return false;
            }
        }

        // Check lower diagonal (left)
        for (int a = row, b = col; a < board.length && b >= 0; a++, b--) {
            if (board[a][b] == 'Q') {
                return false;
            }
        }

        return true;
    }

    public static void saveBoard(List<List<String>> allBoards, char[][] board) {
        List<String> newBoard = new ArrayList<>();

        for (char[] row : board) {
            newBoard.add(new String(row)); // Convert char[] to String
        }

        allBoards.add(newBoard);
    }
}
