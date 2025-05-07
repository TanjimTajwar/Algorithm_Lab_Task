def main():
    # Read the number of test cases
    t = int(input())

    for _ in range(t):
        # Read three integers
        numbers = list(map(int, input().split()))

        # Sort the list
        numbers.sort()

        # The median is the second element in the sorted list
        print(numbers[1])

# Run the function
main()
