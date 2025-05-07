def solve_test_case():
    # Read the number of athletes
    n = int(input())
    
    # Read the strength values of all athletes
    strengths = list(map(int, input().split()))
    
    # Sort the strengths in ascending order
    strengths.sort()
    
    # Initialize minimum difference to the maximum possible difference
    # According to constraints, strength values are between 1 and 1000
    minimum_difference = 1001
    
    # Compare adjacent values to find the minimum difference
    for i in range(1, n):
        current_difference = strengths[i] - strengths[i-1]
        if current_difference < minimum_difference:
            minimum_difference = current_difference
    
    return minimum_difference

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    result = solve_test_case()
    print(result)