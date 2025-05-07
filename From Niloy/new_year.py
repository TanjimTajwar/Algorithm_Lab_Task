def main():
    # Read the positions of the three friends
    x1, x2, x3 = map(int, input().split())
    
    # Sort the positions
    positions = [x1, x2, x3]
    positions.sort()
    
    # The median is the second element after sorting
    median = positions[1]
    
    # Calculate the total distance to the median
    total_distance = abs(x1 - median) + abs(x2 - median) + abs(x3 - median)
    
    # Output the total distance
    print(total_distance)

if __name__ == "__main__":
    main()
