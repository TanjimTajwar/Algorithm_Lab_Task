def solve():
    n, x = map(int, input().split())
    p = [0] * n
    
    if x == 0:
        
        for i in range(1, n):
            p[i-1] = i
        p[n-1] = 0
    elif x == n:
        
        for i in range(n):
            p[i] = i
    else:
       
        i = 0
        for j in range(x):
            p[i] = j
            i += 1
        for j in range(x+1, n):
            p[i] = j
            i += 1
        p[i] = x
    
    print(' '.join(map(str, p)))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()