def solve():
    # Read the number of test cases
    t = int(input())

    for _ in range(t):
        # Read the number of elements in arrays a and b
        n = int(input())
        
        # Read array a
        a = list(map(int, input().split()))
        
        # Read array b
        b = list(map(int, input().split()))
        
        # Count the number of 1s in both arrays
        count_a = sum(a)
        count_b = sum(b)
        
        # Calculate the absolute difference of 1s between a and b
        diff = abs(count_a - count_b)
        
        # Count the number of mismatches between a and b
        mismatch_count = sum(1 for i in range(n) if a[i] != b[i])
        
        # The minimum number of operations required
        min_operations = min(diff + 1, mismatch_count)
        
        # Print the result for this test case
        print(min_operations)

# Run the function
solve()
