t = int(input())
for _ in range(t):
    b = input()
    a = b[0]
    for i in range(1, len(b), 2):
        a += b[i]
    print(a)
