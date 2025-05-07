def solve():
    n = int(input())
    a = list(map(int, input().split()))

    odd_count = 0
    even_count = 0
    for x in a:
        if x % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if odd_count % 2 == 0:
        print(max(a))
    else:
        print(max(a) - 1)

t = int(input())
for _ in range(t):
    solve()