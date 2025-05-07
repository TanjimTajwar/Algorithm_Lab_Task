t = int(input())
for _ in range(t):
    n = int(input())
    given_grid = [list(map(int, input().split())) for _ in range(n)]
    
    sum_of_map = dict()
    bebhorito = set()
    
    for i in range(n):
        for j in range(n):
            s = i + j + 2  
            sum_of_map[s] = given_grid[i][j]
            bebhorito.add(given_grid[i][j])
    
    total = set(range(1, 2 * n + 1))
    answer = (total - bebhorito).pop()
    
    value = [0] * (2 * n + 1)
    value[1] = answer
    for k in range(2, 2 * n + 1):
        value[k] = sum_of_map[k]
    
    print(' '.join(map(str, value[1:])))
