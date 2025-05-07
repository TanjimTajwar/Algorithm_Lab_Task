def main():
    # Read the number of test cases
    t = int(input())
    
    for _ in range(t):
        # Read the length of the array
        n = int(input())
        
        # Read the array of elements
        a = list(map(int, input().split()))
        
        # Sort the array
        a.sort()
        
        # Loop through the sorted array and check for any element appearing at least three times
        for i in range(n - 2):  # We only need to check up to the n-3 index
            if a[i] == a[i + 1] == a[i + 2]:
                print(a[i])
                break
        else:
            # If no value is found, print -1
            print(-1)

if __name__ == "__main__":
    main()
