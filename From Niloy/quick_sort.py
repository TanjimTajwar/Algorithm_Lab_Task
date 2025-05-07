def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    print("Enter the numbers to sort (space-separated integers):")
    arr = list(map(int, input().split()))
    sorted_arr = quicksort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
