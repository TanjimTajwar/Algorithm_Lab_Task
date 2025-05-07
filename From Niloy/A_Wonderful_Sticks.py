def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        count_L = s.count('<')
        count_R = s.count('>')

        small = list(range(1, count_L + 1))
        large = list(range(n - count_R + 1, n + 1))

        used = set(small + large)
        mid = next(i for i in range(1, n + 1) if i not in used)

        demands = ['S' if ch == '<' else 'L' for ch in s]

        ans = [mid]
        i = 0
        while i < len(demands):
            tag = demands[i]
            j = i
            while j < len(demands) and demands[j] == tag:
                j += 1
            length = j - i

            if tag == 'S':
                block = small[-length:]
                small = small[:-length]
                block.sort(reverse=True)
            else:
                block = large[:length]
                large = large[length:]
                block.sort()

            ans.extend(block)
            i = j

        print(*ans)

if __name__ == "__main__":
    main()
