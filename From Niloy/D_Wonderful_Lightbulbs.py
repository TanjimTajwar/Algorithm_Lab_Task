def solve():
    case = int(input())
    for _ in range(case):
        n = int(input())
        x_xor = 0
        sum = 0

        for _ in range(n):
            x, y = map(int, input().split())
            x_xor ^= x
            sum ^= (x + y)

        s = x_xor
        total_possible = sum - s
        print(s, total_possible)

solve()
