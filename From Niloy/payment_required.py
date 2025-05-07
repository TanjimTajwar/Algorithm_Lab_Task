def solve():
    # Read the input values
    n, x = map(int, input().split())
    items = []
    for _ in range(n):
        s, c, p = map(int, input().split())
        items.append((s, c, p))

    # DP array to track the max expected score with a given amount of money
    dp = [0] * (x + 1)

    # Iterate over each item
    for s, c, p in items:
        exp_score = (s * p) / 100.0  # Calculate the expected score for this item

        # Traverse the DP array backwards to avoid overwriting results
        for b in range(x, c - 1, -1):
            dp[b] = max(dp[b], dp[b - c] + exp_score)

    # The result will be the maximum value in the DP array
    print(f"{max(dp):.6f}")

# Call the solve function to read input and compute the result
solve()
