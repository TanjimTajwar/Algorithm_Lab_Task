def draw_snake(n, m):
    # We'll create the grid row by row
    for i in range(n):
        if i % 2 == 0:
            # For odd-indexed rows (0, 2, 4,...), move from left to right
            print('#' * m)
        else:
            # For even-indexed rows (1, 3, 5,...), move from right to left
            print('#' * m)

# Read input
n, m = map(int, input().split())

# Draw the snake
draw_snake(n, m)
