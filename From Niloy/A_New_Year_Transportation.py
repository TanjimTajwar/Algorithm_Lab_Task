n, t = map(int, input().split())
a = list(map(int, input().split()))

position = 1

while position < t:
    position += a[position-1]

if position == t:
    print("YES")
else:
    print("NO")
