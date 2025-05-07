def max_middle_class(n, x, wealth):
    wealth.sort(reverse=True)  # Sort wealth in descending order
    total = 0
    count = 0

    for i in range(n):
        total += wealth[i]
        if total >= (count + 1) * x:  # Check if average meets or exceeds x
            count += 1
        else:
            break  # Stop early if adding more people drops average below x

    return count

# Input handling
t = int(input())  # Number of test cases

for _ in range(t):
    n, x = map(int, input().split())  # Number of people and minimum wealth threshold
    wealth = list(map(int, input().split()))  # Wealth of each person
    print(max_middle_class(n, x, wealth))
