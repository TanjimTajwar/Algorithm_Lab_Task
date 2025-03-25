def bubble_sort(arr):
    num=len(arr)
    for a in range (num-1):
        for b in range (num-a-1):
            if(is_small(arr,b,b+1)):
                arr[b],arr[b+1]=arr[b+1],arr[b]

def is_small(arr,a,b):
    return arr[a]>arr[b]


num = int(input("Enter the number of element in the Array: "))
arr = list(map(int,input("Enter the elements of Array: ").split()))

print("UnSorted Array: " , arr)

bubble_sort(arr)

print("Sorted Array: " , arr)
