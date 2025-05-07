n = int(input())
magnets = [input().strip() for _ in range(n)]

groups = 1  # The first magnet starts the first group

for i in range(1, n):
    if magnets[i] != magnets[i - 1]:  # A new group forms when polarity changes
        groups += 1

print(groups)
