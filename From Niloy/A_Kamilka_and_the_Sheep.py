def max_pleasure(n, beauty_levels):
    
    diffs = []
    for i in range(n):
        for j in range(i+1, n):
            diffs.append(abs(beauty_levels[i] - beauty_levels[j]))
    
    
    diffs = sorted(set(diffs), reverse=True)
    
    
    for diff in diffs:
        
        divisors = []
        i = 1
        while i*i <= diff:
            if diff % i == 0:
                divisors.append(i)
                if i != diff // i:
                    divisors.append(diff // i)
            i += 1
        
        
        divisors.sort(reverse=True)
        
       
        for d in divisors:
            
            remainders = {}
            for beauty in beauty_levels:
                r = beauty % d
                if r in remainders:
                    return d  
                remainders[r] = True
    
    return 1  


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    beauty_levels = list(map(int, input().split()))
    print(max_pleasure(n, beauty_levels))