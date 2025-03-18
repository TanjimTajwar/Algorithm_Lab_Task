#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function to check if a queen can be placed on board[row][col]
bool isSafe(vector<vector<char>>& board, int row, int col, int n) {
    // Check left side of row
    for (int j = 0; j < col; j++) {
        if (board[row][j] == 'Q') {
            return false;
        }
    }
    
    // Check upper diagonal (left)
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 'Q') {
            return false;
        }
    }
    
    // Check lower diagonal (left)
    for (int i = row, j = col; i < n && j >= 0; i++, j--) {
        if (board[i][j] == 'Q') {
            return false;
        }
    }
    
    return true;
}

// Function to save the current board configuration
void saveBoard(vector<vector<string>>& allBoards, vector<vector<char>>& board) {
    vector<string> newBoard;
    for (const auto& row : board) {
        newBoard.push_back(string(row.begin(), row.end()));
    }
    allBoards.push_back(newBoard);
}

// Helper function to solve N Queens problem
void helper(vector<vector<char>>& board, vector<vector<string>>& allBoards, int col, int n) {
    // Base case: if all queens are placed
    if (col == n) {
        saveBoard(allBoards, board);
        return;
    }
    
    // Try placing queen in each row of current column
    for (int row = 0; row < n; row++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 'Q';  // Place queen
            helper(board, allBoards, col + 1, n);  // Recur for next column
            board[row][col] = '.';  // Backtrack
        }
    }
}

// Main function to solve N Queens problem
vector<vector<string>> findNQueen(int n) {
    vector<vector<string>> allBoards;
    vector<vector<char>> board(n, vector<char>(n, '.'));
    
    helper(board, allBoards, 0, n);
    return allBoards;
}

int main() {
    int n;
    cout << "Enter the number of Queens: ";
    cin >> n;
    
    vector<vector<string>> solutions = findNQueen(n);
    
    cout << "The pattern for " << n << " Queen problem is:" << endl;
    for (const auto& board : solutions) {
        for (const auto& row : board) {
            cout << row << endl;
        }
        cout << endl;
    }
    
    return 0;
} 