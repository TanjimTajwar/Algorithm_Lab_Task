# Read the number of test cases
t = int(input())

# Loop over all test cases
for _ in range(t):
    # Read the list of participant strengths
    strengths = list(map(int, input().split()))
    
    # Sort the array in descending order
    sorted_strengths = sorted(strengths, reverse=True)
    
    # The maximum and second maximum strength
    max_strength = sorted_strengths[0]
    second_max_strength = sorted_strengths[1]
    
    # For each participant, calculate the difference
    result = []
    for s in strengths:
        if s == max_strength:
            # If the participant is the strongest, subtract the second max
            result.append(s - second_max_strength)
        else:
            # Otherwise, subtract the max strength
            result.append(s - max_strength)
    
    # Print the result for the current test case
    print(" ".join(map(str, result)))
