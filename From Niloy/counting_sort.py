def counting_sort(arr):
    if not arr:
        return []

    # Find the range of input
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Update count[i] so that count[i] contains actual position
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)

'''taking input'''
def counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count and output arrays
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Count the occurrences
    for num in arr:
        count[num - min_val] += 1

    # Update the count array to store positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the sorted output
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output

def main():
    print("Enter the numbers to sort (space-separated integers):")
    arr = list(map(int, input().split()))

    sorted_arr = counting_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
