n = int(input())
count = 0

for _ in range(n):
    pi, qi = map(int, input().split())
    if qi - pi >= 2:
        count += 1

print(count)
