def max_toasts(n, k, l, c, d, p, nl, np):
    total_drink = k * l
    total_slices = c * d
    total_salt = p

    toasts_from_drink = total_drink // (nl * n)
    toasts_from_limes = total_slices // n
    toasts_from_salt = total_salt // (np * n)

    return min(toasts_from_drink, toasts_from_limes, toasts_from_salt)

# Input
n, k, l, c, d, p, nl, np = map(int, input().split())

# Output
print(max_toasts(n, k, l, c, d, p, nl, np))
