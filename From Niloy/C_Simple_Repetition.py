def solve():
    x, k = map(int, input().split())
    if k == 1:
        if x > 1:
            prime_ki_hobe = True
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    prime_ki_hobe = False
                    break
            if prime_ki_hobe:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
        return

    if k > 1:
        if k == 2:
            if x == 3 or x == 9:
                print("NO")
                return
        if k == 3:
            if x == 3:
                print("NO")
                return
        if k == 4:
            print("NO")
            return
        if k == 5:
            if x % 5 == 0:
                print("NO")
                return
        if k == 6:
            print("NO")
            return
        if k == 7:
            if x == 3:
                print("NO")
                return

        string_of_x = str(x)
        n_x = len(string_of_x)
        string_of_y = string_of_x * k
        y = int(string_of_y)

        if y <= 1:
            print("NO")
            return

        prime_ki_hobe = True
        for i in range(2, int(y**0.5) + 2):
            if y % i == 0:
                prime_ki_hobe = False
                break
        if prime_ki_hobe:
            print("YES")
        else:
            print("NO")
        return


t = int(input())
for _ in range(t):
    solve()