def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = 0
    prev = 0
    for val in arr:
        ans = max(ans, val - prev)
        prev = val

    ans = max(ans, 2 * (k - prev))
    print(ans)

t = int(input())
for _ in range(t):
    solve()
