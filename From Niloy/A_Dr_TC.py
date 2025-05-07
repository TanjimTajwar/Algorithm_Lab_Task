t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count_of_1 = s.count('1')
    total = count_of_1 * (count_of_1 - 1) + (n - count_of_1) * (count_of_1 + 1)
    print(total)
