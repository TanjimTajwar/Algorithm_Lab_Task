def interesting():
    size = int(input())
    elements = list(map(int, input().split()))
    
    target = [0, 1, 0, 3, 2, 0, 2, 5]
    
    for i in range(1, size + 1):
        draw = elements[:i]
        
        count = {}
        for d in draw:
            count[d] = count.get(d, 0) + 1
        
        target_count = {}
        for t in target:
            target_count[t] = target_count.get(t, 0) + 1
        
        can = True
        for d, c in target_count.items():
            if count.get(d, 0) < c:
                can = False
                break
        
        if can:
            print(i)
            return
    
    print(0)

i = int(input())
for _ in range(i):
    interesting()