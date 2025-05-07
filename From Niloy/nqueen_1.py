def solve_n_queens(n):
    solutions = []

    def is_safe(queens, row, col):
        for r in range(row):
            c = queens[r]
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def backtrack(row, queens):
        if row == n:
            solutions.append(queens[:])  # save a copy of the solution
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                backtrack(row + 1, queens)
                queens[row] = -1  # backtrack

    # Start solving
    backtrack(0, [-1] * n)

    # Print all solutions
    for sol in solutions:
        for row in sol:
            line = [' 1 '] * n
            line[row] = ' 0 '
            print(''.join(line))
        print()

    # Print count
    print("Total solutions:", len(solutions))

# Example usage
solve_n_queens(4)
