import sys
input = sys.stdin.read

data = input().split()
i = 0

n = int(data[i]); i += 1
m = int(data[i]); i += 1

used_in = [[] for _ in range(n + 1)]  
left = []  


for d in range(m):
    k = int(data[i]); i += 1
    ing = list(map(int, data[i:i + k]))
    i += k
    left.append(k)
    for x in ing:
        used_in[x].append(d)

b = list(map(int, data[i:]))  

done = [False] * m 
cnt = 0
res = []

for x in b:
    for d in used_in[x]:
        left[d] -= 1
        if left[d] == 0 and not done[d]:
            cnt += 1
            done[d] = True
    res.append(str(cnt))

print("\n".join(res))
