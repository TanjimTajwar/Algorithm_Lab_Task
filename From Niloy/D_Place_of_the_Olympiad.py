def solve():
    import sys
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    t = int(data[0].strip())
    out_lines = []
    
    
    def row_max(m, L):
        
        g0 = (m + 1) // (L + 1)
        p1 = g0 * L
        
        if g0 < m:
            p2 = min((g0 + 1) * L, m - g0)
        else:
            p2 = p1
        return max(p1, p2)
    
    for i in range(1, t + 1):
        n, m, k = map(int, data[i].split())
        
        
        low, high = 1, m
        ans = -1
        
        
        while low <= high:
            mid = (low + high) // 2
            capacity = n * row_max(m, mid)
            if capacity >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        out_lines.append(str(ans))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
