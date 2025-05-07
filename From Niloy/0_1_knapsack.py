def knapsack_01(values, weights, capacity):
    n = len(values)
    # Initialize DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Max of taking or not taking the current item
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# 👇 USER INPUT SECTION 👇
n = int(input("Enter number of items: "))
values = []
weights = []

print("Enter value and weight for each item:")
for i in range(n):
    v = int(input(f"  Value of item {i+1}: "))
    w = int(input(f"  Weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = int(input("Enter knapsack capacity: "))

# ✅ Solve and print result
max_value = knapsack_01(values, weights, capacity)
print(f"\nMaximum value that can be carried: {max_value}")

'''1D approach'''

print("1D approach")
def knapsack_01_1d(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]

# 👇 USER INPUT SECTION 👇
n = int(input("Enter number of items: "))
values = []
weights = []

print("Enter value and weight for each item:")
for i in range(n):
    v = int(input(f"  Value of item {i+1}: "))
    w = int(input(f"  Weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = int(input("Enter knapsack capacity: "))

# ✅ Solve and print result
max_value = knapsack_01_1d(values, weights, capacity)
print(f"\nMaximum value that can be carried: {max_value}")


