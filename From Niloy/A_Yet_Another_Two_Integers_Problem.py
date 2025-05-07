
t = int(input())


for _ in range(t):
    a, b = map(int, input().split())  
    diff = abs(a - b)  
    moves = diff // 10 + (1 if diff % 10 != 0 else 0)
    print(moves)
