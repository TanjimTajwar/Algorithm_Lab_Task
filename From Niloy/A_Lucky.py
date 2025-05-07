t=int(input())

for _ in range(t):
    values=list(map(int,input()))
    first_three=sum(values[:3])
    last_three=sum(values[3:])
    
    if first_three==last_three:
        print("YES")

    else:
        print("NO")