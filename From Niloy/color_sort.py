def sortColors(nums):
    n = len(nums)
    
    # Bubble sort-like approach, but specifically for sorting 0s, 1s, and 2s
    for i in range(n):
        for j in range(0,n-1):
            if nums[j] > nums[j+1]:
                # Swap adjacent elements if they're in the wrong order
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums

n=list(map(int,input().split()))

print(sortColors(n))