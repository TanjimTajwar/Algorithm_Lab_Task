# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the values of n and m
    n, m = map(int, input().split())

    # Read the wealth values
    wealth = list(map(int, input().split()))

    # Sort the wealth in descending order
    wealth.sort(reverse=True)

    # Initialize sum and count
    total_sum = 0
    count = 0

    # Iterate through sorted wealth
    for i in range(n):
        total_sum += wealth[i]
        count += 1

        # Check if the average is at least m
        if total_sum / count < m:
            count -= 1  # Remove the last person (since they dropped the average)
            break

    # Print the maximum number of people
    print(count)
