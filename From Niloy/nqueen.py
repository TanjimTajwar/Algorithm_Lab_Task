def solve_n_queens(n):
    board = [-1] * n  # board[i] = column of queen in row i

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def place_queen(row):
        if row == n:
            return True  # Found a valid placement
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if place_queen(row + 1):
                    return True
                board[row] = -1  # backtrack
        return False

    if place_queen(0):
        print_board(board)
    else:
        print("No solution found.")

def print_board(board):
    n = len(board)
    for row in range(n):
        line = [' 0 '] * n
        line[board[row]] = ' Q '
        print(''.join(line))
    print()

# Example usage
solve_n_queens(5)
