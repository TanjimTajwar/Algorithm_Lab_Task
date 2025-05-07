def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        swapped = False  # Flag to check if any swaps occurred
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, then the list is already sorted
        if not swapped:
            break
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the pivot (middle element)
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    return quicksort(left) + middle + quicksort(right)

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Compare adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)

def merge_sort(arr):
    # Base case: a list of one element is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the array
    mid = len(arr) // 2
    left_half = arr[:mid]  # Left half of the array
    right_half = arr[mid:]  # Right half of the array

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))  # Pop the smaller element from left
        else:
            sorted_arr.append(right.pop(0))  # Pop the smaller element from right

    # If there are remaining elements in either left or right, append them
    sorted_arr.extend(left)
    sorted_arr.extend(right)

    return sorted_arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # The element to be inserted
        j = i - 1  # Index of the previous element
        # Shift elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key element at the correct position
        arr[j + 1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)


def counting_sort(arr):
    # If the array is empty, return it as is
    if len(arr) == 0:
        return arr
    
    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)
    
    # Create a count array with size of (max_val - min_val + 1)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element in the count array
    for num in arr:
        count[num - min_val] += 1

    # Modify the count array by adding the previous counts (cumulative sum)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array using the count array
    for num in reversed(arr):  # Iterate in reverse to maintain stability
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    # Copy the sorted elements back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)


def bucket_sort(arr):
    # If the array is empty, return it as is
    if len(arr) == 0:
        return arr
    
    # Step 1: Create n empty buckets
    n = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / n  # Size of each bucket
    
    # Create empty buckets (list of lists)
    buckets = [[] for _ in range(n)]
    
    # Step 2: Distribute elements into the buckets
    for num in arr:
        index = int((num - min_value) // bucket_range)
        if index == n:  # Handle the case where num is the maximum value
            index -= 1
        buckets[index].append(num)
    
    # Step 3: Sort each bucket using Python's built-in sort (or sorted())
    for i in range(n):
        buckets[i].sort()  # Sort each bucket in place
    
    # Step 4: Concatenate all the sorted buckets into a single array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

arr = [0.42, 0.32, 0.23, 0.55, 0.64, 0.75, 0.12]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)


def insertion_sort(arr):
    """Helper function to perform Insertion Sort on each bucket."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr):
    # If the array is empty, return it as is
    if len(arr) == 0:
        return arr
    
    # Step 1: Create n empty buckets
    n = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / n  # Size of each bucket
    
    # Create empty buckets (list of lists)
    buckets = [[] for _ in range(n)]
    
    # Step 2: Distribute elements into the buckets
    for num in arr:
        index = int((num - min_value) // bucket_range)
        if index == n:  # Handle the case where num is the maximum value
            index -= 1
        buckets[index].append(num)
    
    # Step 3: Sort each bucket
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])
    
    # Step 4: Concatenate all the sorted buckets into a single array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

arr = [0.42, 0.32, 0.23, 0.55, 0.64, 0.75, 0.12]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)


def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_val = max(arr)
    
    # Start from the least significant digit (1's place) and move to higher places
    exp = 1  # exp will represent the place value (1, 10, 100, 1000,...)
    
    # Continue until we've processed all digits
    while max_val // exp > 0:
        # Create 10 buckets (for digits 0 to 9)
        buckets = [[] for _ in range(10)]
        
        # Place elements into respective buckets based on the current digit
        for num in arr:
            index = (num // exp) % 10  # Get the current digit
            buckets[index].append(num)
        
        # Reconstruct the array by concatenating elements from all buckets
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        
        # Move to the next digit place (exp increases by a factor of 10)
        exp *= 10
    
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)
