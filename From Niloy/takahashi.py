from collections import deque

Q = int(input())
queue = deque()

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        X = int(query[1])
        queue.append(X)
    elif query[0] == '2':
        print(queue.popleft())
