n, k = map(int, input().split())
scores = list(map(int, input().split()))

for score in scores:
    count=0
    if score>=k:
        count+=1

print(count)