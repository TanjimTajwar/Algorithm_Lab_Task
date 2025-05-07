def max_problems(n, k):
    time_left = 240 - k
    total_time = 0
    count = 0

    for i in range(1, n + 1):
        total_time += 5 * i
        if total_time > time_left:
            break
        count += 1

    return count

# Read input
n, k = map(int, input().split())
print(max_problems(n, k))
