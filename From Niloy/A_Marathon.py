t = int(input())
for _ in range(t):
    values = list(map(int, input().split()))
    count = 0
    a=values[0]
    for x in values[1:]:
        if x > a:
            count += 1
    print(count)
