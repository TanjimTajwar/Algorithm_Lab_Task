def solve():
    n = int(input())
    q = int(input())
    size = 1 << n

    def get_value(r, c, n_level):
        if n_level == 0:
            if r == 0 and c == 0:
                return 1
            elif r == 1 and c == 1:
                return 2
            elif r == 1 and c == 0:
                return 3
            elif r == 0 and c == 1:
                return 4
        else:
            sub_size = 1 << (n_level - 1)
            if r < sub_size and c < sub_size:
                return get_value(r, c, n_level - 1)
            elif r >= sub_size and c >= sub_size:
                return (1 << (2 * (n_level - 1))) + get_value(r - sub_size, c - sub_size, n_level - 1)
            elif r >= sub_size and c < sub_size:
                return 2 * (1 << (2 * (n_level - 1))) + get_value(r - sub_size, c, n_level - 1)
            elif r < sub_size and c >= sub_size:
                return 3 * (1 << (2 * (n_level - 1))) + get_value(r, c - sub_size, n_level - 1)

    def get_coords(d, n_level):
        if n_level == 0:
            if d == 1:
                return 0, 0
            elif d == 2:
                return 1, 1
            elif d == 3:
                return 1, 0
            elif d == 4:
                return 0, 1
        else:
            sub_area = 1 << (2 * (n_level - 1))
            sub_size = 1 << (n_level - 1)
            if d <= sub_area:
                r, c = get_coords(d, n_level - 1)
                return r, c
            elif d <= 2 * sub_area:
                r, c = get_coords(d - sub_area, n_level - 1)
                return r + sub_size, c
            elif d <= 3 * sub_area:
                r, c = get_coords(d - 2 * sub_area, n_level - 1)
                return r + sub_size, c
            else:
                r, c = get_coords(d - 3 * sub_area, n_level - 1)
                return r, c + sub_size

    for _ in range(q):
        query = input().split()
        if query[0] == '>':
            r = int(query[1]) - 1
            c = int(query[2]) - 1
            print(get_value(r, c, n))
        elif query[0] == '<':
            d = int(query[1])
            r, c = get_coords(d, n)
            print(r + 1, c + 1)

t = int(input())
for _ in range(t):
    solve()