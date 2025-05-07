def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    
    for l in range(1, n-1):
        left_subarray = a[:l]
        left_median = sorted(left_subarray)[(len(left_subarray)+1)//2 - 1]
        
        
        if left_median <= k:
           
            for r in range(l+1, n):
                mid_subarray = a[l:r]
                right_subarray = a[r:]
                
                mid_med = sorted(mid_subarray)[(len(mid_subarray)+1)//2 - 1]
                right_med = sorted(right_subarray)[(len(right_subarray)+1)//2 - 1]
                
                if mid_med <= k or right_med <= k:
                    return "YES"
        
        
        else:
            for r in range(l+1, n):
                mid_subarray = a[l:r]
                right_subarray = a[r:]
                
                mid_med = sorted(mid_subarray)[(len(mid_subarray)+1)//2 - 1]
                right_med = sorted(right_subarray)[(len(right_subarray)+1)//2 - 1]
                
                if mid_med <= k and right_med <= k:
                    return "YES"
    
    return "NO"

t=int(input())
for _ in range(t):
   print(solve())