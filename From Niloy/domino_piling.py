def max_dominoes(length, breadth):
    # Calculate the area of the grid
    area = length * breadth
    
    # Each domino covers 2 square units
    domino_area = 2
    
    # Calculate the maximum number of dominoes that can fit in the grid
    max_dominoes = area // domino_area
    
    return max_dominoes

# Input length and breadth of the grid
length = int(input("Enter the length of the grid: "))
breadth = int(input("Enter the breadth of the grid: "))

# Calculate and print the maximum number of dominoes
print("Maximum number of dominoes that can fit in the grid:", max_dominoes(length, breadth))