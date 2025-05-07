def cases():
    n = int(input())
    a = list(map(int, input().split()))
    distinct = set(a)
    return len(distinct)

t = int(input())
for _ in range(t):
    print(cases())