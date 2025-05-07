def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    res = []

    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2

        l = list(map(int, data[idx:idx + n]))
        idx += n
        r = list(map(int, data[idx:idx + n]))
        idx += n

        pairs = []
        extras = 0
        total = 0

        for i in range(n):
            p = min(l[i], r[i])
            pairs.append((p, l[i] + r[i]))
        
        # Sort by how many pairs we can make (descending)
        pairs.sort(reverse=True)

        # Take top k pairs (the best colors to form pairs)
        gloves_needed = 0
        for i in range(k):
            gloves_needed += pairs[i][1] - 1  # worst case: miss 1 glove

        gloves_needed += 1  # +1 to ensure the first pair is complete in worst case

        res.append(str(gloves_needed))

    print("\n".join(res))

solve()