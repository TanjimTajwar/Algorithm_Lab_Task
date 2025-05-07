from collections import deque
import sys
input = sys.stdin.read

data = input().split()
idx = 0
t = int(data[idx])
idx += 1

res = []

for _ in range(t):
    q = int(data[idx])
    idx += 1
    arr = deque()

    for _ in range(q):
        s = int(data[idx])
        idx += 1

        if s == 1:  # cyclic shift
            arr.appendleft(arr.pop())
        elif s == 2:  # reverse
            arr.reverse()
        else:  # s == 3 (append)
            k = int(data[idx])
            idx += 1
            arr.append(k)

        # Recalculate rizziness
        rizz = sum(arr[i] * (i + 1) for i in range(len(arr)))
        res.append(str(rizz))

print("\n".join(res))
