def pack(z):
    if not z:
        return []
    out = []
    ch = z[0]
    cnt = 1
    for c in z[1:]:
        if c == ch:
            cnt += 1
        else:
            out.append((ch, cnt))
            ch = c
            cnt = 1
    out.append((ch, cnt))
    return out

for _ in range(int(input())):
    a = input().strip()
    b = input().strip()

    if not (len(a) <= len(b) <= 2 * len(a)):
        print("NO")
        continue

    x = pack(a)
    y = pack(b)

    if len(x) != len(y):
        print("NO")
        continue

    ok = all(x[i][0] == y[i][0] and x[i][1] <= y[i][1] <= 2 * x[i][1] for i in range(len(x)))
    print("YES" if ok else "NO")
