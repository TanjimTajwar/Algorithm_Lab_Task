import sys


def solve():
    
    n, k = map(int, sys.stdin.readline().split())
    
    a = list(map(int, sys.stdin.readline().split()))
    
    b = list(map(int, sys.stdin.readline().split()))

    
    min_x = 0
    
    max_x = k + k 

    
    for i in range(n):
       
        curr_min = 0
        curr_max = k + k 

        if b[i] != -1:
            
            curr_sum = a[i] + b[i]
            curr_min = curr_sum
            curr_max = curr_sum
        else:
            
            curr_min = a[i]
            curr_max = a[i] + k

        
        min_x = max(min_x, curr_min)
        max_x = min(max_x, curr_max)

        
        if min_x > max_x:
            print(0)
            return

    
    print(max(0, max_x - min_x + 1))



T = int(sys.stdin.readline())

for _ in range(T):
    solve()