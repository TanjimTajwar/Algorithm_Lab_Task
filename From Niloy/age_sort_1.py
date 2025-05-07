def sort_ages():
    # List to store all results
    all_results = []
    
    while True:
        # Read the number of people
        n = int(input())
        
        # Check for termination condition (n = 0)
        if n == 0:
            break
        
        # Read the ages
        ages = list(map(int, input().split()))
        
        # Sort the ages
        sorted_ages = sorted(ages)
        
        # Store the result for later output
        all_results.append(' '.join(map(str, sorted_ages)))
    
    # Print all results at once after termination
    for result in all_results:
        print(result)

# Call the function
sort_ages()