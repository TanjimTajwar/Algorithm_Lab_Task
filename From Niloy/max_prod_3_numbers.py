# Take input for the array
nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Sort the array in ascending order
nums.sort()

# The three largest numbers are the last three elements
# The two smallest numbers are the first two elements
# Calculate the maximum product considering the two cases:
# 1. Product of the three largest numbers
# 2. Product of the two smallest numbers and the largest number
result = max(
    nums[-1] * nums[-2] * nums[-3],  # Product of the three largest numbers
    nums[0] * nums[1] * nums[-1]    # Product of two smallest and the largest number
)

print("Maximum product:", result)
