def intersection(nums1, nums2):
    # Step 1: Convert both lists to sets to remove duplicates
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Step 2: Create an empty list to store the intersection
    result = []
    
    # Step 3: Iterate through one set and check if the element is in the other set
    for num in set1:
        if num in set2:
            result.append(num)
    
    return result

# Taking input from the user
nums1 = list(map(int, input("Enter the elements of nums1 separated by space: ").split()))
nums2 = list(map(int, input("Enter the elements of nums2 separated by space: ").split()))

# Call the function and print the result
print("Intersection:", intersection(nums1, nums2))
