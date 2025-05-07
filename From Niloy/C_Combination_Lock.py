def solve():
    n = int(input())
    if n % 2 == 0:
        print(-1)
        return

    result = []
    for i in range(n):
        result.append((2 * i + 1) % n + 1)

    print(*result)

t = int(input())
for _ in range(t):
    solve()