# Input the array
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Calculate the number of elements to remove
remove_nos = int(len(arr) * 0.05)

# Sort the array
arr.sort()

# Remove 5% of the smallest and largest elements
arr = arr[remove_nos:len(arr) - remove_nos]

# Calculate the mean manually
mean_value = sum(arr) / len(arr)

# Print the result
print(mean_value)

# Input the array
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Specify the elements to remove
elements_to_remove = list(map(int, input("Enter the elements to remove separated by spaces: ").split()))

# Remove the specified elements from the array
arr = [x for x in arr if x not in elements_to_remove]

# Calculate the mean of the remaining elements
if len(arr) > 0:  # Prevent division by zero if the array is empty
    mean_value = sum(arr) / len(arr)
    print(mean_value)
else:
    print("No elements left in the array.")
