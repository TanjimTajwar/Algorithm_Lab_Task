def solve():
    n = int(input())
    s = list(input())

    def is_balanced(arr):
        counts = {'L': 0, 'I': 0, 'T': 0}
        for char in arr:
            counts[char] += 1
        return len(set(counts.values())) == 1

    ops = []
    for _ in range(2 * n):
        if is_balanced(s):
            print(len(ops))
            for op in ops:
                print(op)
            return

        changed = False
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                insert_char = None
                for char in 'LIT':
                    if char != s[i] and char != s[i + 1]:
                        insert_char = char
                        break

                s.insert(i + 1, insert_char)
                ops.append(i + 1)
                changed = True
                break
        if not changed:
            break

    if is_balanced(s):
        print(len(ops))
        for op in ops:
            print(op)
    else:
        print(-1)

t = int(input())
for _ in range(t):
    solve()