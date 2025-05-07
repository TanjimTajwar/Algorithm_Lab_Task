def sort_ages():
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
        
        # Print the sorted ages with space separation
        print(' '.join(map(str, sorted_ages)))

# Call the function
sort_ages()