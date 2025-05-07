
n = int(input()) 
p = list(map(int, input().split())) 


average_percentage = sum(p) / n


print(f"{average_percentage:.12f}")
