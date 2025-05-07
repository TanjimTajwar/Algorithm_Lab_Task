t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    max_len = 1
    curr_len = 1

    for i in range(1, n):
        if a[i] - a[i-1] <= k:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1  # Restart the segment

    print(n - max_len)
