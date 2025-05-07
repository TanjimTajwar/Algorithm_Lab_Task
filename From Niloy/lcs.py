def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct LCS from the DP table
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()  # Reverse to get correct order
    return dp[m][n], ''.join(lcs_str)

# 👇 USER INPUT 👇
X = input("Enter first string: ")
Y = input("Enter second string: ")

# ✅ Output
length, lcs_sequence = lcs(X, Y)
print(f"Length of LCS: {length}")
print(f"LCS string: {lcs_sequence}")
