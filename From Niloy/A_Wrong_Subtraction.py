n, k = map(int, input().split())

for _ in range(k):
    if n % 10 != 0:
        n -= 1  # Remove the last digit if it's zero
    else:
        n //= 10  # Subtract one if the last digit is non-zero

print(n)
