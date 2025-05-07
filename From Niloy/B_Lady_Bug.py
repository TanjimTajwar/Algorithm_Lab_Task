def solve():
    n = int(input())
    a = input().strip()
    b = input().strip()

    if a[0] == '1':
        print("NO")
        return

    a_list = list(a)
    b_list = list(b)

    ones_a = []
    for i in range(n):
        if a_list[i] == '1':
            ones_a.append(i)

    for index_a in ones_a:
        swapped = False
        if index_a > 0 and b_list[index_a-1] == '1':
            a_list[index_a], b_list[index_a-1] = b_list[index_a-1], a_list[index_a]
            swapped = True
        elif index_a > 1 and a_list[index_a-1] == '1':
            a_list[index_a-1], b_list[index_a] = b_list[index_a], a_list[index_a-1]
            swapped = True

        if not swapped:
            print("NO")
            return

    if all(x == '0' for x in a_list):
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()