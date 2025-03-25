def insertionSort(arr):
    num = len(arr)
    for a in range (1,num):
        b=a-1
        key=arr[a]
        while b>=0  and arr[b]>key:
            arr[b+1]=arr[b]
            b=b-1
        arr[b+1]=key 



num = int(input("Enter Number of Elements inside Array: "))
arr = list(map(int,input("Enter the elements of the Array: ").split()))

insertionSort(arr)
print("Sorted Array: ")
print(*arr)