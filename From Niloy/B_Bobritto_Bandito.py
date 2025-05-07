def solve():
    n, m, l, r = map(int, input().split())
    new_l = -l
    maybe_r = min(m, new_l)
    print(-maybe_r, m - maybe_r)

t = int(input())
for _ in range(t):
    solve()
