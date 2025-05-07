t = int(input())
ks = [int(input()) for _ in range(t)]

# Precompute liked numbers
liked = []
i = 1
while len(liked) < max(ks):  # Generate up to max k needed
    if i % 3 != 0 and i % 10 != 3:
        liked.append(i)
    i += 1

# Output the k-th liked number for each test case
for k in ks:
    print(liked[k - 1])
