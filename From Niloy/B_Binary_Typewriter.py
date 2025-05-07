def calc(s):
    finger = '0'  
    cost = 0
    
    for char in s:
        if char != finger:
            cost += 1 
            finger = char
        cost += 1 
    
    return cost

def case():
    n = int(input())
    s = input().strip()
    
    
    original_cost = calc(s)
    minimum = original_cost
    
    
    for l in range(n):
        for r in range(l, n):
            
            if r - l > 20 and n > 100:
                continue
                
            new_s = s[:l] + s[l:r+1][::-1] + s[r+1:]
            cost = calc(new_s)
            minimum = min(minimum, cost)
    
    return minimum

t = int(input())
for _ in range(t):
    print(case())