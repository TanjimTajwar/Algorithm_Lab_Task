def can_defeat_all_dragons(s, dragons):
    # Sort dragons by strength
    dragons.sort()

    for x, y in dragons:
        if s > x:
            s += y  # Gain bonus strength
        else:
            return "NO"  # Kirito loses

    return "YES"  # Kirito defeats all dragons

# Read initial strength and number of dragons
s, n = map(int, input().split())

# Read dragon data in a simpler way
dragons = []
for _ in range(n):
    x, y = map(int, input().split())  # Read dragon strength and bonus
    dragons.append((x, y))  # Store as a tuple

# Output result
print(can_defeat_all_dragons(s, dragons))
