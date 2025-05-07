def is_safe(board, row, col):
    """Checks if placing a queen at board[row][col] is safe."""

    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board), 1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, solutions):
    """Recursive utility function to solve the N-Queens problem."""

    n = len(board)
    if row == n:
        # Found a solution!
        solutions.append([list(row) for row in board])  # Append a copy
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            solve_n_queens_util(board, row + 1, solutions)
            board[row][col] = 0  # Backtrack: remove queen

def solve_n_queens(n):
    """Solves the N-Queens problem for a given board size n."""
    board = [[0 for _ in range(n)] for _ in range(n)]  # Initialize board
    solutions = []
    solve_n_queens_util(board, 0, solutions)
    return solutions

# Example usage:
n = 8
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(row)
    print("-" * 10)