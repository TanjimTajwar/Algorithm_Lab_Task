
def read_data():
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))

    tableau = [[0.0 for _ in range(n+1)] for _ in range(m)]
    print(f"Enter coefficients (enter 'q' when finished):")

    for i in range(m):
        for j in range(n):
            while True:
                val = input(f"Row {i}, Column {j}: ")
                if val.lower() == 'q':
                    return m, n, tableau
                try:
                    tableau[i][j] = float(val)
                except ValueError:
                    print("Invalid value. Please enter a number.")

    for i in range(m):
        tableau[i][-1] = 1.0

    return m, n, tableau


def find_entering_variable(tableau, m, n):
    pivot_element = min([row[n-1] for row in tableau])
    pivot_row = [i for i, x in enumerate([row[n-1] for row in tableau]) if x == pivot_element][0]

    return pivot_row


def find_leaving_variable(tableau, m, n):
    pivot_column = [min([tableau[i][j] for i in range(m)]) for j in range(n)].index(min(map(min, [tableau[i][:n-1]
for i in range(m)])))

    return pivot_column


def perform_pivot_operation(tableau, pivot_row, pivot_column):
    tableau[pivot_row][pivot_column] = 1/tableau[pivot_row][pivot_column]

    for i in range(m):
        if i != pivot_row:
            multiplier = tableau[i][pivot_column]
            for j in range(n+1):
                tableau[i][j] -= multiplier * tableau[pivot_row][j]

    return tableau


def solve_lp(tableau, m, n):
    solution = [0.0 for _ in range(n)]

    for i in range(n-1):
        pivot_row = find_entering_variable(tableau, m, n)
        pivot_column = find_leaving_variable(tableau, m, n)

        tableau = perform_pivot_operation(tableau, pivot_row, pivot_column)

    return solution


def main():
    m, n, tableau = read_data()

    while True:
        if max([row[n-1] for row in tableau]) > 0.0001:
            break
        else:
            tableau = perform_pivot_operation(tableau, find_entering_variable(tableau, m, n),
find_leaving_variable(tableau, m, n))

    solution = solve_lp(tableau, m, n)

    print(f"Optimal Solution: {solution}")


if __name__ == "__main__":
    main()
