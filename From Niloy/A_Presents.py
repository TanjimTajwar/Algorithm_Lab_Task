def solve():
    # Read number of friends
    n = int(input())
    
    # Read the list of who gave gifts to whom
    p = list(map(int, input().split()))
    
    # Create an array to store the results
    result = [0] * n
    
    # Reverse the mapping: for each i, find who gave a gift to i
    for i in range(n):
        result[p[i] - 1] = i + 1  # We subtract 1 and add 1 to work with 1-indexed results
    
    # Print the result
    print(" ".join(map(str, result)))

# Execute the function
solve()
