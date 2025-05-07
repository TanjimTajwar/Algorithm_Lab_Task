# Input the array
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Sort the array
arr.sort()

# Initialize the minimum difference
minDiff = arr[1] - arr[0]

# Find the minimum absolute difference
for i in range(len(arr) - 1):
    minDiff = min(minDiff, arr[i + 1] - arr[i])

# Create a list to store pairs with the minimum difference
result = []

# Add the pairs with the minimum difference to the result
for i in range(len(arr) - 1):
    if arr[i + 1] - arr[i] == minDiff:
        result.append([arr[i], arr[i + 1]])

# Print the result
print(result)
