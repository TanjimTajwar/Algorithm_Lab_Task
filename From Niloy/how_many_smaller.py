def smallerNumbersThanCurrent(nums):
    # Step 1: Sort the array and store it
    sorted_nums = sorted(nums)
    
    # Step 2: Create an empty result array
    result = []

    # Step 3: For each number in the original array, count how many are smaller
    for num in nums:
        count = 0  # Initialize counter
        for sorted_num in sorted_nums:
            if num > sorted_nums:  # Count numbers smaller than current number
                count += 1
            else:
                break  # No need to check further since array is sorted
        result.append(count)  # Store the count
    
    return result

# Taking input from the user
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by spaces: ").split()))

# Call the function and print the result
print("Output:", smallerNumbersThanCurrent(nums))
