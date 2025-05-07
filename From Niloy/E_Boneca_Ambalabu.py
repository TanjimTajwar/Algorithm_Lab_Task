import sys
import numpy as np
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = np.array(list(map(int, input().split())), dtype=np.uint32)

    b = 30
    c = np.zeros(b, dtype=np.uint32)

    for j in range(b):
        c[j] = np.count_nonzero((a >> j) & 1)

    uttor = 0
    for v in a:
        s = 0
        for j in range(b):
            m = 1 << j
            if (v >> j) & 1:
                s += (n - c[j]) * m
            else:
                s += c[j] * m
        uttor = max(uttor, s)

    sys.stdout.write(str(uttor) + "\n")
