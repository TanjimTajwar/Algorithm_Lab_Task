def solve():
    import sys, bisect
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    t = int(data[0])
    
    
    ns = []
    for i in range(1, t+1):
        parts = data[i].split()
        n = int(parts[0])
        ns.append(n)
    
    max_n = max(ns)
    
    
    sieve = bytearray(b'\x01') * (max_n + 1)
    sieve[:2] = b'\x00\x00'
    primes = []
    for i in range(2, max_n+1):
        if sieve[i]:
            primes.append(i)
            step = i
            
            sieve[i*i:max_n+1:step] = b'\x00' * (((max_n - i*i) // step) + 1)
    
    
    
    out_lines = []
    for n in ns:
        
        r = bisect.bisect_right(primes, n)
        ans = 0
        i = 0
        
        while i < r:
            v = n // primes[i]
            
            lo, hi = i, r - 1
            j = i
            while lo <= hi:
                mid = (lo + hi) // 2
                if n // primes[mid] == v:
                    j = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            count = j - i + 1
            ans += count * v
            i = j + 1
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
