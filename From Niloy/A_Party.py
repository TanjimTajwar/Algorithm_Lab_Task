n=int(input())

p=[int(input()) for _ in range(n)]

depth=[0]*n

def get_depth(i):
    if depth[i]!=0:
        return depth[i]
    elif p[i] == -1:
        depth[i]=1
    else:
        depth[i]=1+get_depth(p[i]-1)
    return depth[i]

max_depth=0

for i in range(n):
    max_depth=max(max_depth,get_depth(i))

print(max_depth)