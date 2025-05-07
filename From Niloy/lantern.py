def main():
    # Read input values
    n, l = map(int, input().split())
    lanterns = list(map(int, input().split()))
    
    # Sort the positions of the lanterns
    lanterns.sort()
    
    # Calculate the maximum gap between consecutive lanterns
    max_gap = 0
    for i in range(1, n):
        max_gap = max(max_gap, lanterns[i] - lanterns[i - 1])
    
    # The gap at the ends of the street
    gap_at_start = lanterns[0] - 0
    gap_at_end = l - lanterns[-1]
    
    # The minimum radius d is the maximum of:
    # - Half of the largest gap between consecutive lanterns
    # - The distance from the first lantern to the start of the street
    # - The distance from the last lantern to the end of the street
    d = max(max_gap / 2, gap_at_start, gap_at_end)
    
    # Print the result with a precision of 9 decimal places
    print(f"{d:.9f}")

if __name__ == "__main__":
    main()
