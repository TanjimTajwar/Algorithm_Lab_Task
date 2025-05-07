# Take space-separated input and convert it to a list of integers
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sort the list
nums.sort()

n = len(nums)

if n == 0:  # Handle empty input case
    print("No numbers were entered.")
else:
    # Find the median
    if n % 2 == 1:  # Odd length: take the middle element
        median = nums[n // 2]
    else:  # Even length: average the two middle elements
        median = (nums[n // 2] + nums[n // 2 - 1]) / 2

    # Print the integer part of the median
    print(int(median))  # Convert to integer to remove fractional part
