def min_bills(n):
    denominations = [100, 20, 10, 5, 1]
    count = 0
    for d in denominations:
        count += n // d
        n %= d
    return count


n = int(input())
print(min_bills(n))
