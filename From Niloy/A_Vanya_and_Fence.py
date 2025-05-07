
n, h = map(int, input().split())  
a = list(map(int, input().split()))  


width = 0
for height in a:
    if height <= h:
        width += 1
    else:
        width += 2


print(width)
