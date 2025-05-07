def rearrange_array(n, arr):
    arr.sort()  # Step 1: Sort the array

    # Step 2: Find the middle index
    mid = (n - 1) // 2  

    # Step 3: Rearrange the array using two pointers
    result = []
    left = mid  # Start from the middle
    right = mid + 1  # Element just after the middle

    while left >= 0 or right < n:
        if left >= 0:
            result.append(arr[left])  # Add left element
            left -= 1
        if right < n:
            result.append(arr[right])  # Add right element
            right += 1

    # Step 4: Print the rearranged array
    print(" ".join(map(str, result)))

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read input values
    n = int(input())  # Number of elements in array
    arr = list(map(int, input().split()))  # Read array elements

    # Call function to process the array
    rearrange_array(n, arr)
