def max_water(n, k, barrels):
    barrels.sort()  # Sort barrels in ascending order
    return sum(barrels[-(k+1):])  # Sum the largest k+1 elements

# Read number of test cases
t = int(input())

for _ in range(t):
    # Read n (number of barrels) and k (number of moves)
    n, k = map(int, input().split())

    # Read the barrel water amounts
    barrels = list(map(int, input().split()))

    # Print the maximum water possible in the smallest barrel
    print(max_water(n, k, barrels))
