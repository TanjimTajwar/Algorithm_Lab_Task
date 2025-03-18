import java.util.Scanner

// Function to check if a queen can be placed on board[row][col]
fun isSafe(board: Array<CharArray>, row: Int, col: Int, n: Int): Boolean {
    // Check left side of row
    for (j in 0 until col) {
        if (board[row][j] == 'Q') {
            return false
        }
    }
    
    // Check upper diagonal (left)
    var i = row
    var j = col
    while (i >= 0 && j >= 0) {
        if (board[i][j] == 'Q') {
            return false
        }
        i--
        j--
    }
    
    // Check lower diagonal (left)
    i = row
    j = col
    while (i < n && j >= 0) {
        if (board[i][j] == 'Q') {
            return false
        }
        i++
        j--
    }
    
    return true
}

// Function to save the current board configuration
fun saveBoard(allBoards: MutableList<List<String>>, board: Array<CharArray>) {
    val newBoard = board.map { it.joinToString("") }
    allBoards.add(newBoard)
}

// Helper function to solve N Queens problem
fun helper(board: Array<CharArray>, allBoards: MutableList<List<String>>, col: Int, n: Int) {
    // Base case: if all queens are placed
    if (col == n) {
        saveBoard(allBoards, board)
        return
    }
    
    // Try placing queen in each row of current column
    for (row in 0 until n) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 'Q'  // Place queen
            helper(board, allBoards, col + 1, n)  // Recur for next column
            board[row][col] = '.'  // Backtrack
        }
    }
}

// Main function to solve N Queens problem
fun findNQueen(n: Int): List<List<String>> {
    val allBoards = mutableListOf<List<String>>()
    val board = Array(n) { CharArray(n) { '.' } }
    
    helper(board, allBoards, 0, n)
    return allBoards
}

fun main() {
    val scanner = Scanner(System.`in`)
    
    print("Enter the number of Queens: ")
    val n = scanner.nextInt()
    
    val solutions = findNQueen(n)
    
    println("The pattern for $n Queen problem is:")
    for (board in solutions) {
        for (row in board) {
            println(row)
        }
        println()
    }
    
    scanner.close()
} 