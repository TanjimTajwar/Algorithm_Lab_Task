def find_optimal_location():
    # Read the number of test cases
    test_cases = int(input())
    
    # Process each test case
    for _ in range(test_cases):
        # Read relative information
        relatives_info = list(map(int, input().split()))
        num_relatives = relatives_info[0]
        street_numbers = relatives_info[1:]
        
        # Sort the street numbers
        street_numbers.sort()
        
        # Find the median position
        median_position = street_numbers[num_relatives // 2]
        
        # Calculate total distance
        total_distance = 0
        for street in street_numbers:
            total_distance = total_distance + abs(street - median_position)
        
        # Print the result
        print(total_distance)

# Run the solution
find_optimal_location()