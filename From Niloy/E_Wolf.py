def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        p = list(map(int, input().split()))
        pos = [0] * (n + 1)
        for i in range(n):
            pos[p[i]] = i + 1

        for _ in range(q):
            l, r, x = map(int, input().split())
            px = pos[x]
            if px < l or px > r:
                print(-1)
                continue

            low, high = l, r
            Ml = Mg = M = Lg = Gg = 0

            while low <= high:
                m = (low + high) // 2
                if m == px:
                    break
                if m < px:
                    if p[m - 1] < x:
                        Lg += 1
                    else:
                        Ml += 1
                        M += 1
                    low = m + 1
                else:
                    if p[m - 1] > x:
                        Gg += 1
                    else:
                        Mg += 1
                        M += 1
                    high = m - 1

            tl = x - 1
            tg = n - x
            sl = tl - Lg
            sg = tg - Gg

            if Ml > sl or Mg > sg:
                print(-1)
            else:
                print(M + abs(Ml - Mg))

main()
