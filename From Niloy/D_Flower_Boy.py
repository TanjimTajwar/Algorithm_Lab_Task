def match(x, y):
    i = 0
    for v in y:
        while i < len(x) and x[i] < v:
            i += 1
        if i == len(x):
            return False
        i += 1
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        u = list(map(int, input().split()))
        v = list(map(int, input().split()))
        
        if match(u, v):
            print(0)
            continue

        l, r = 1, max(max(u), max(v))
        ans = -1

        while l <= r:
            z = (l + r) // 2
            ok = False
            for j in range(n + 1):
                w = u[:j] + [z] + u[j:]
                if match(w, v):
                    ok = True
                    break
            if ok:
                ans = z
                r = z - 1
            else:
                l = z + 1

        print(ans)

solve()
