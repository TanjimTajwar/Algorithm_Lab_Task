
def findKthLargest(nums):
        # Create a copy of the original array to avoid modifying the original array
        nums_copy = nums.copy()
        
        # Sort the copied array in non-decreasing order
        nums_copy.sort()
        
        # Return the k-th largest element from the sorted array (access from the end)
        return nums_copy[-k]

# Example usage:
nums = list(map(int,input().split()))
k = int(input())

# Create an instance of Solution and call the method


print(findKthLargest(nums))
