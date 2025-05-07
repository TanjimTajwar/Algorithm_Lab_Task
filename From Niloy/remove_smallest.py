def main():
    # Read the number of test cases
    t = int(input())

    for _ in range(t):
        # Read the number of elements in the array
        n = int(input())
        
        # Read the array elements and convert them into a list of integers
        a = list(map(int, input().split()))
        
        # Sort the array in non-decreasing order
        a.sort()

        # Check if it is possible to make all elements equal by repeatedly subtracting 1
        possible = True

        for i in range(1, n):
            # If the difference between consecutive elements is more than 1, it's impossible
            if abs(a[i] - a[i - 1])> 1:
                possible = False
                break
        
        # Print "YES" if possible, otherwise print "NO"
        if possible:
            print("YES")
        else:
            print("NO")

# Run the function
main()
