n, k = map(int, input().split())
participations = list(map(int, input().split()))

eligible_students = sum(1 for p in participations if p <= 5 - k)

# Maximum teams that can be formed
print(eligible_students // 3)
