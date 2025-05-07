def solve():
    n, m, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            grid[i][j] = (count % k) + 1
            count += 1

    for r in range(n):
        for c in range(m):
            original_val = grid[r][c]
            for val in range(1, k + 1):
                valid = True
                if val == original_val:
                    continue
                if r > 0 and grid[r - 1][c] == val:
                    valid = False
                if r < n - 1 and grid[r + 1][c] == val:
                    valid = False
                if c > 0 and grid[r][c - 1] == val:
                    valid = False
                if c < m - 1 and grid[r][c + 1] == val:
                    valid = False
                if valid:
                    grid[r][c] = val
                    break

    for row in grid:
        print(*row)

t = int(input())
for _ in range(t):
    solve()