n = int(input())  # Read the size of the array
arr = list(map(int, input().split()))  # Read the array elements

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]  # Swap if arr[i] > arr[j]
            cnt += 1  # Increment the swap count

print("Optimal train swapping takes %d swaps." % cnt)
